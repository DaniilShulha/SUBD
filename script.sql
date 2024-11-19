CREATE TABLE category (
    id serial primary key,
    category_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE country (
    id serial primary key,
    country_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE manufacturer (
    id serial primary key,
    name VARCHAR(255) NOT NULL,
    country_id INTEGER NOT NULL REFERENCES country(id) ON DELETE CASCADE, -- Удаление производителя при удалении страны
    CONSTRAINT manufacturer_name_country_unique UNIQUE (name, country_id) -- Имя производителя должно быть уникальным в пределах страны
);

CREATE TABLE instrument (
    id serial primary key,
    instrument_name VARCHAR(255) NOT NULL,
    category_id INTEGER NOT NULL REFERENCES category(id) ON DELETE CASCADE, -- Удаление инструмента при удалении категории
    manufacturer_id INTEGER NOT NULL REFERENCES manufacturer(id) ON DELETE SET NULL, -- Установка NULL при удалении производителя
    description TEXT CHECK (LENGTH(description) <= 255), -- Ограничение длины текста
    CONSTRAINT instrument_name_category_unique UNIQUE (instrument_name, category_id)
);

CREATE TABLE item (
    id serial primary key,
    serial_number VARCHAR(255) NOT NULL UNIQUE, -- Уникальные серийные номера
    instrument_id INTEGER NOT NULL REFERENCES instrument(id) ON DELETE CASCADE, -- Удаление предмета при удалении инструмента
    description TEXT CHECK (LENGTH(description) <= 255), -- Ограничение длины текста
    year_of_production INT NOT NULL CHECK (year_of_production >= 1900 AND year_of_production <= EXTRACT(YEAR FROM NOW())), -- Год от 1900 до текущего
    country_id INTEGER NOT NULL REFERENCES country(id) ON DELETE SET NULL, -- Установка NULL при удалении страны
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0)
);

CREATE TABLE role (
    id serial primary key,
    role_name VARCHAR(255) NOT NULL UNIQUE
);


CREATE TABLE users (
    id serial primary key,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE, -- Уникальные email
    password VARCHAR(255) NOT NULL CHECK (LENGTH(password) >= 8), -- Минимальная длина пароля 8 символов
    country_id INTEGER REFERENCES country(id) ON DELETE SET NULL, -- Установка NULL при удалении страны
    role_id INTEGER REFERENCES role(id) ON DELETE SET NULL
);



CREATE TABLE review (
    id serial primary key,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Удаление отзыва при удалении пользователя
    instrument_id INTEGER NOT NULL REFERENCES instrument(id) ON DELETE CASCADE, -- Удаление отзыва при удалении инструмента
    description TEXT CHECK (LENGTH(description) <= 255), -- Ограничение длины текста
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5) -- Рейтинг от 1 до 5
);



CREATE TABLE order_status (
    id serial primary key,
    status_name VARCHAR(255) NOT NULL UNIQUE -- Уникальные названия статусов заказов
);

CREATE TABLE customer_order (
    id serial primary key,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Удаление заказа при удалении пользователя
    order_time TIMESTAMP NOT NULL DEFAULT NOW(),
    delivery_address VARCHAR(255) NOT NULL,
    preffered_delivery_time TIMESTAMP,
    order_status_id INTEGER NOT NULL REFERENCES order_status(id) ON DELETE SET NULL, -- Установка NULL при удалении статуса заказа
    time_paid TIMESTAMP,
    time_canceled TIMESTAMP,
    time_completed TIMESTAMP,
    total_price DECIMAL(10, 2) NOT NULL CHECK (total_price >= 0), -- Общая цена должна быть неотрицательной
    discount DECIMAL(10, 2) DEFAULT 0 CHECK (discount >= 0), -- Скидка должна быть неотрицательной
    active BOOLEAN NOT NULL DEFAULT TRUE -- Указывает, активен ли заказ
);



CREATE TABLE payment (
    id serial primary key,
    customer_order_id INTEGER NOT NULL REFERENCES customer_order(id) ON DELETE CASCADE, -- Удаление платежа при удалении заказа
    payment_method VARCHAR(255) NOT NULL,
    payment_status VARCHAR(255) NOT NULL
);



CREATE TABLE order_item (
    id serial primary key,
    customer_order_id INTEGER NOT NULL REFERENCES customer_order(id) ON DELETE CASCADE, -- Удаление строки заказа при удалении заказа
    item_id INTEGER NOT NULL REFERENCES item(id) ON DELETE CASCADE, -- Удаление строки заказа при удалении предмета
    quantity INT NOT NULL CHECK (quantity > 0) -- Количество должно быть положительным

);