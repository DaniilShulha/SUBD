
-- 1. Trigger to update total_price in customer_order when order_item is added/modified
CREATE OR REPLACE FUNCTION update_order_total()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE customer_order
    SET total_price = (
        SELECT COALESCE(SUM(i.price * oi.quantity), 0)
        FROM order_item oi
        JOIN item i ON oi.item_id = i.id
        WHERE oi.customer_order_id = NEW.customer_order_id
    )
    WHERE id = NEW.customer_order_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER order_total_update
AFTER INSERT OR UPDATE ON order_item
FOR EACH ROW
EXECUTE FUNCTION update_order_total();

-- 2. Trigger to log all changes to customer_order status
CREATE TABLE order_status_log (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    old_status_id INTEGER,
    new_status_id INTEGER NOT NULL,
    change_time TIMESTAMP DEFAULT NOW(),
    user_id INTEGER NOT NULL
);

CREATE OR REPLACE FUNCTION log_order_status_change()
RETURNS TRIGGER AS $$
BEGIN
    IF (NEW.order_status_id != OLD.order_status_id) THEN
        INSERT INTO order_status_log (order_id, old_status_id, new_status_id, user_id)
        VALUES (NEW.id, OLD.order_status_id, NEW.order_status_id, NEW.user_id);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER order_status_change_log
AFTER UPDATE ON customer_order
FOR EACH ROW
EXECUTE FUNCTION log_order_status_change();

-- 3. Trigger to automatically set time_paid when order status changes to paid
CREATE OR REPLACE FUNCTION update_payment_time()
RETURNS TRIGGER AS $$
BEGIN
    IF (NEW.payment_status = 'Оплачено' AND OLD.payment_status != 'Оплачено') THEN
        UPDATE customer_order
        SET time_paid = NOW()
        WHERE id = NEW.customer_order_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER payment_time_update
AFTER UPDATE ON payment
FOR EACH ROW
EXECUTE FUNCTION update_payment_time();

-- 4. Trigger to prevent deletion of items with active orders
CREATE OR REPLACE FUNCTION prevent_item_deletion()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM order_item oi
        JOIN customer_order co ON oi.customer_order_id = co.id
        WHERE oi.item_id = OLD.id AND co.active = true
    ) THEN
        RAISE EXCEPTION 'Cannot delete item with active orders';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER item_deletion_protection
BEFORE DELETE ON item
FOR EACH ROW
EXECUTE FUNCTION prevent_item_deletion();

-- 5. Trigger to validate review ratings and automatically update review statistics
CREATE TABLE instrument_review_stats (
    instrument_id INTEGER PRIMARY KEY,
    total_reviews INTEGER DEFAULT 0,
    avg_rating DECIMAL(3,2) DEFAULT 0
);

CREATE OR REPLACE FUNCTION update_review_stats()
RETURNS TRIGGER AS $$
BEGIN
    -- Validate rating
    IF NEW.rating NOT BETWEEN 1 AND 5 THEN
        RAISE EXCEPTION 'Rating must be between 1 and 5';
    END IF;
    
    -- Update or insert stats
    INSERT INTO instrument_review_stats (instrument_id, total_reviews, avg_rating)
    VALUES (
        NEW.instrument_id,
        1,
        NEW.rating
    )
    ON CONFLICT (instrument_id) DO UPDATE
    SET total_reviews = instrument_review_stats.total_reviews + 1,
        avg_rating = (
            SELECT AVG(rating)::DECIMAL(3,2)
            FROM review
            WHERE instrument_id = NEW.instrument_id
        );
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER review_stats_update
AFTER INSERT ON review
FOR EACH ROW
EXECUTE FUNCTION update_review_stats();

-- 6. Trigger to enforce business hours for order processing
CREATE OR REPLACE FUNCTION validate_order_time()
RETURNS TRIGGER AS $$
DECLARE
    current_hour INTEGER;
BEGIN
    current_hour := EXTRACT(HOUR FROM CURRENT_TIME);
    
    -- Allow orders only between 9 AM and 9 PM
    IF current_hour < 9 OR current_hour >= 21 THEN
        RAISE EXCEPTION 'Orders can only be placed between 9:00 AM and 9:00 PM';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER order_time_validation
BEFORE INSERT ON customer_order
FOR EACH ROW
EXECUTE FUNCTION validate_order_time();