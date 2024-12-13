
-- 1. Процедура для регистрации нового пользователя
CREATE OR REPLACE PROCEDURE register_user(
    p_user_name VARCHAR(255),
    p_email VARCHAR(255),
    p_password VARCHAR(255),
    p_country_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO users (user_name, email, password, country_id, role_id)
    VALUES (p_user_name, p_email, p_password, p_country_id, 1); -- role_id = 1 для обычных пользователей
END;
$$;

-- 2. Процедура для обновления цены товара
CREATE OR REPLACE PROCEDURE update_item_price(
    p_item_id INTEGER,
    p_new_price DECIMAL
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_new_price <= 0 THEN
        RAISE EXCEPTION 'Цена должна быть больше нуля';
    END IF;

    UPDATE item
    SET price = p_new_price
    WHERE id = p_item_id;
END;
$$;

-- 3. Процедура для отмены заказа
CREATE OR REPLACE PROCEDURE cancel_order(
    p_order_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE customer_order
    SET order_status_id = 7, -- Статус "Отменен"
        time_canceled = NOW(),
        active = FALSE
    WHERE id = p_order_id
    AND order_status_id NOT IN (6, 7); -- Нельзя отменить доставленный или уже отмененный заказ
END;
$$;

-- 4. Процедура для изменения роли пользователя
CREATE OR REPLACE PROCEDURE change_user_role(
    p_user_id INTEGER,
    p_new_role_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM role WHERE id = p_new_role_id) THEN
        RAISE EXCEPTION 'Указанная роль не существует';
    END IF;

    UPDATE users
    SET role_id = p_new_role_id
    WHERE id = p_user_id;
END;
$$;

-- 5. Процедура для добавления нового инструмента в каталог
CREATE OR REPLACE PROCEDURE add_new_instrument(
    p_name VARCHAR(255),
    p_category_id INTEGER,
    p_manufacturer_id INTEGER,
    p_description TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF LENGTH(p_description) > 255 THEN
        RAISE EXCEPTION 'Описание слишком длинное';
    END IF;

    INSERT INTO instrument (instrument_name, category_id, manufacturer_id, description)
    VALUES (p_name, p_category_id, p_manufacturer_id, p_description);
END;
$$;

-- Примеры использования:

-- Регистрация нового пользователя
-- CALL register_user('Иван', 'ivan@example.com', 'password123', 1);

-- Обновление цены товара
-- CALL update_item_price(1, 299.99);

-- Отмена заказа
-- CALL cancel_order(1);

-- Изменение роли пользователя
-- CALL change_user_role(1, 2);

-- Добавление нового инструмента
-- CALL add_new_instrument('Yamaha C40', 1, 6, 'Классическая гитара начального уровня');