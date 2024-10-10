CREATE TABLE category (
    id serial primary key,
    category_name varchar(255)
);

CREATE TABLE country (
    id serial primary key,
    country_name varchar(255)
);

CREATE TABLE manufacturer (
    id serial primary key,
    name varchar(255),
    country_id integer REFERENCES country(id)
);

CREATE TABLE instrument (
    id serial primary key,
    instrument_name varchar(255),
    category_id integer REFERENCES category(id),
    manufacturer_id integer REFERENCES manufacturer(id),
    description text(255)
);

CREATE TABLE item (
    id serial primary key,
    serial_number varchar(255),
    instrument_id integer REFERENCES instrument(id),
    description text(255),
    year_of_production int,
    country_id integer REFERENCES country(id),
    price decimal(10, 2)
);

CREATE TABLE role (
    id serial primary key,
    role_name varchar(255)
);

CREATE TABLE user (
    id serial primary key,
    user_name varchar(255),
    email varchar(255),
    password varchar(255),
    country_id integer REFERENCES country(id),
    role_id integer REFERENCES role(id)
);

CREATE TABLE review (
    id serial primary key,
    user_id integer REFERENCES user(id),
    instrument_id integer REFERENCES instrument(id),
    description text(255),
    rating integer CHECK (rating >= 1 AND rating <= 5)
);

CREATE TABLE order_status (
    id serial primary key,
    status_name varchar(255)
);

CREATE TABLE customer_order (
    id serial primary key,
    user_id integer REFERENCES user(id),
    order_time timestamp,
    delivery_address varchar(255),
    preffered_delivery_time timestamp,
    order_status_id integer REFERENCES order_status(id),
    time_paid timestamp,
    time_canceled timestamp,
    time_completed timestamp,
    total_price decimal(10, 2),
    discount decimal(10, 2),
    active boolean
);

CREATE TABLE payment (
    id serial primary key,
    customer_order_id integer REFERENCES customer_order(id),
    payment_method varchar(255),
    payment_status varchar(255)
);

CREATE TABLE order_item (
    id serial primary key,
    customer_order_id integer REFERENCES customer_order(id),
    item_id integer REFERENCES item(id),
    quantity int
);
