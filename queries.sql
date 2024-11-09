SELECT * FROM users
--
SELECT * FROM users
WHERE email = 'alexey.petrov@example.com'
--

INSERT INTO users (user_name, email, password, country_id, role_id)
VALUES (
        'Виталий',
        'Vitaliy@example.com',
        'DfTsgw',
		6,
		1
    );
--
UPDATE users
SET password = 'newpassword123'
WHERE email = 'Vitaliy@example.com';
--
DELETE FROM users
WHERE id = 12;
--
INSERT INTO customer_order (user_id, order_time, delivery_adress, preffered_delivery_time, order_status_id, time_paid, time_canceled, time_completed, total_price, discount, active)
VALUES (
    1,
    '2024-12-21 19:30:00',
    '8962 Music Ave, New York, NY, USA',
    '2024-12-24 10:00:00',
    3,
    '2024-12-21 19:45:00',
    NULL,
    NULL,
    420,
    25,
    TRUE
);
--

UPDATE customer_order
SET order_time = '2024-12-21 19:40:00'
WHERE id = 5;
--

SELECT * FROM item
WHERE serial_number = 'EKO-700V-2024-001';
--

SELECT serial_number, description, price
FROM item
--

INSERT INTO item (serial_number, instrument_id, description, year_of_production, price)
VALUES
(
	'SAV-540J-2022-341',
	28,
	'Viscount Legend — электронный орган, созданный итальянской компанией Viscount, отличается реалистичным звуком и имитацией классического тон-колеса. Оснащен качественными моделями звукового генератора.',
	2006,
	325
)
--

SELECT * FROM instrument
WHERE id BETWEEN 25 AND 40;
--

SELECT instrument_name
FROM instrument
ORDER BY instrument_name ASC;

UPDATE item
SET price = price * 1.5
WHERE id = 3;
--

SELECT * FROM instrument
WHERE category_id = 2 AND manufacturer_id = 2;