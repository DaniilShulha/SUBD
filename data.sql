INSERT INTO role (id, role_name)
VALUES
    (1, 'customer'),
    (2, 'manager'),
    (3, 'administrator');

INSERT INTO category (id, category_name)
VALUES
    (1, 'Струнные'),
    (2, 'Духовые'),
    (3, 'Ударные'),
    (4, 'Клавишные'),
    (5, 'Электронные');

INSERT INTO country (id, country_name)
VALUES
    (1, 'США'),
    (2, 'Япония'),
    (3, 'Италия'),
    (4, 'Германия'),
    (5, 'Франция'),
    (6, 'Россия'),
    (7, 'Украина'),
    (8, 'Беларусь'),
    (9, 'Казахстан'),
    (10, 'Литва');

INSERT INTO order_status (id, status_name)
VALUES
    (1, 'В обработке'),
    (2, 'Подтвержден'),
    (3, 'На складе'),
    (4, 'Отправлен'),
    (5, 'В пути'),
    (6, 'Доставлен'),
    (7, 'Отменен'),
    (8, 'Возврат');

INSERT INTO manufacturer (id, name, country_id)
VALUES
    (1, 'Gibson', 1),
    (2, 'Conn-Selmer', 1),
    (3, 'DW Drums', 1),
    (4, 'Steinway & Sons', 1),
    (5, 'Moog', 1),
    (6, 'Yamaha', 2),
    (7, 'Kawai', 2),
    (8, 'Roland', 2),
    (9, 'Eko', 3),
    (10, 'Rampone & Cazzani', 3),
    (11, 'UFIP', 3),
    (12, 'D-Viscount', 3),
    (13, 'Höfner', 4),
    (14, 'Sonor', 4),
    (15, 'Buffet Crampon', 4),
    (16, 'Bechstein', 4),
    (17, 'Savarez', 5),
    (18, 'Selmer', 5),
    (19, 'Asba', 5),
    (20, 'Pleyel', 5);

INSERT INTO instrument (id, instrument_name, manufacturer_id, category_id, description)
VALUES
    (1, 'Gibson Les Paul Standard', 1, 1, 'Электрогитара'),
    (2, 'Gibson J-45', 1, 1, 'Акустическая гитара'),
    (3, 'Selmer Mark VI', 2, 2, 'Саксофон'),
    (4, 'Conn 8D', 2, 2, 'Французский рожок'),
    (5, 'Gibson SG', 3, 3, 'Барабанная установка'),
    (6, 'DW Performance Series', 3, 3, 'Барабанная установка'),
    (7, 'Steinway Model D', 4, 4, 'Рояль'),
    (8, 'Steinway Model S', 4, 4, 'Рояль'),
    (9, 'Moog Minimoog Model D', 5, 5, 'Синтезатор'),
    (10, 'Moog Sub 37', 5, 5, 'Синтезатор'),
    (11, 'Yamaha Pacifica 112V', 6, 1, 'Электрогитара'),
    (12, 'Yamaha LL16', 6, 1, 'Акустическая гитара'),
    (13, 'Yamaha Stage Custom Birch', 6, 3, 'Ударная установка'),
    (14, 'Yamaha Recording Custom', 6, 3, 'Ударная установка'),
    (15, 'Yamaha YFL-222', 6, 2, 'Флейта'),
    (16, 'Yamaha YAS-62', 6, 2, 'Альт-саксофон'),
    (17, 'Kawai K-300', 7, 4, 'Пианино'),
    (18, 'Kawai GX-3', 7, 4, 'Рояль'),
    (19, 'Roland Jupiter-8', 8, 5, 'Синтезатор'),
    (20, 'Roland TR-808', 8, 5, 'Ритм-машина'),
    (21, 'Eko Ranger 6', 9, 1, 'Акустическая гитара'),
    (22, 'Eko 700V', 9, 1, 'Электрогитара'),
    (23, 'Rampone & Cazzani R1 Jazz', 10, 2, 'Саксофон'),
    (24, 'Rampone & Cazzani Vintage', 10, 2, 'Саксофон'),
    (25, 'UFIP Class Series', 11, 3, 'Тарелки'),
    (26, 'UFIP Natural Series', 11, 3, 'Тарелки'),
    (27, 'Viscount Cantorum V', 12, 4, 'Электронный орган'),
    (28, 'Viscount Legend', 12, 4, 'Электронный орган'),
    (29, 'Höfner 500/1 Violin Bass', 13, 1, 'Бас-гитара'),
    (30, 'Höfner Verythin', 13, 1, 'Электрогитара'),
    (31, 'Sonor SQ2', 14, 3, 'Ударная установка'),
    (32, 'Sonor Vintage Series', 14, 3, 'Ударная установка'),
    (33, 'Buffet Crampon R13', 15, 2, 'Кларнет'),
    (34, 'Buffet Crampon E12F', 15, 2, 'Кларнет'),
    (35, 'Bechstein Model B', 16, 4, 'Пианино'),
    (36, 'Bechstein Concert 8', 16, 4, 'Пианино'),
    (37, 'Savarez 520R ', 17, 1, 'Струны для классической гитары'),
    (38, 'Savarez 540J', 17, 1, 'Струны для акустической гитары'),
    (39, 'Selmer Super Action 80 Series II', 18, 2, 'Саксофон'),
    (40, 'Selmer Reference 54', 18, 2, 'Саксофон'),
    (41, 'Asba Revelation', 19, 3, 'Ударная установка'),
    (42, 'Asba Caroline', 19, 3, 'Малый барабан'),
    (43, 'Pleyel Model P', 20, 4, 'Пианино'),
    (44, 'Pleyel Grand Piano', 20, 4, 'Рояль');

INSERT INTO users (id, user_name, email, password, country_id, role_id)
VALUES
    (1, 'Алексей', 'alexey.petrov@example.com', 'DfT#92x@Q!', 6, 1),
    (2, 'Виктория', 'viktoria.ivanova@example.com', 'hM6*7#e@S!', 7, 1),
    (3, 'Дмитрий', 'dmitriy.ivanov@example.com', 'bT5%99c@A!', 8, 1),
    (4, 'Михаил', 'michael.petrov@example.com', 'jK9#2a@F!', 9, 1),
    (5, 'Наталья', 'natalia.petrova@example.com', 'xT6%4f@M!', 1, 1),
    (6, 'Олег', 'oleg.ivanov@example.com', 'sR7%7g@U!', 10, 1),
    (7, 'Павел', 'pavel.petrov@example.com', 'pK6%4d@R!', 7, 2),
    (8, 'Сергей', 'sergey.ivanov@example.com', 'zT5%99c@G!', 8, 2),
    (9, 'Admin', 'admin@example.com', 'kT6%4f@O!', 8, 3);

INSERT INTO review (id, user_id, instrument_id, description, rating)
VALUES
    (1, 1, 5, 'Установка Gibson SG — это настоящее чудо! Звучание мощное и чистое, а качество материалов на высоте. Идеально подходит для всех стилей музыки. Рекомендую всем музыкантам!', 5),
    (2, 2, 34, 'Кларнет Buffet Crampon E12F имеет хорошее звучание и приятную игру, но качество сборки оставляет желать лучшего. Некоторые детали требуют улучшения, и в целом инструмент не оправдал моих ожиданий.', 3),
    (3, 6, 22, 'Электрогитара Eko 700V радует своим винтажным звучанием и стильным дизайном. Удобная в игре, но иногда возникают проблемы с настройкой. В целом, отличное соотношение цены и качества!', 4),
    (4, 6, 16, 'Хотелось бы больше от Yamaha YAS-62. Звучание неплохое, но инструмент не всегда отвечает на нюансы игры. К тому же, качество сборки оставляет желать лучшего. Не оправдал ожиданий.', 2);

INSERT INTO item (id, instrument_id, serial_number, description, year_of_production, country_id, price)
VALUES
    (1, 22, 'EKO-700V-2024-001', 'Электрогитара Eko 700V предлагает винтажный дизайн и мощное звучание. Удобный гриф и высококачественные датчики делают ее идеальной для различных стилей музыки. Отличный выбор для начинающих и опытных музыкантов!', 1960, 3, 200),
    (2, 38, 'SAV-540J-2024-001', 'Акустическая гитара Savarez 540J предлагает насыщенное и теплое звучание, идеально подходящее для игры в различных музыкальных стилях. С качественными материалами и удобным грифом, она обеспечивает комфорт и выразительность в исполнении. Отличный выбор для начинающих и опытных музыкантов, стремящихся к качественному звучанию!', 2005, 5, 60),
    (3, 11, 'YAM-PAC112V-2024-001', 'Yamaha Pacifica 112V — универсальная электрогитара с отличным звучанием. Удобный гриф и трехпозиционный переключатель обеспечивают легкость игры в различных стилях. Идеальный выбор для начинающих и опытных музыкантов!', 2014, 2, 150),
    (4, 7, 'STE-MD-2024-001', 'Steinway Model D — это выдающийся концертный рояль, известный своим богатым и мощным звучанием. Его выдающаяся техника и элегантный дизайн делают его идеальным выбором для профессиональных музыкантов и концертных залов.', 2001, 1, 400);

INSERT INTO customer_order (id, user_id, order_time, delivery_adress, preffered_delivery_time, order_status_id, time_paid, time_canceled, time_completed, total_price, discount, active)
VALUES
    (1, 1, '2024-09-08 14:30:00', '1234 Music Ave, New York, NY, USA', '2024-09-10 10:00:00', 2, '2024-09-08 14:45:00', NULL, NULL, 400, 25, TRUE),
    (2, 2, '2024-08-15 16:00:00', '5678 Melody Lane, Los Angeles, CA, USA', '2024-08-20 15:30:00', 1, '2024-08-11 09:15:00', NULL, NULL, 60, 50, TRUE),
    (3, 3, '2024-07-22 18:45:00', '9876 Harmony Blvd, Chicago, IL, USA', '2024-07-25 12:00:00', 5, '2024-07-23 11:30:00', NULL, NULL, 150, 15, TRUE),
    (4, 4, '2024-06-25 11:15:00', '4321 Rhythm Rd, Miami, FL, USA', '2024-06-30 09:00:00', 7, '2024-06-25 13:00:00', '2024-06-26 10:00:00', '2024-06-26 12:00:00', 200, 15, FALSE);


INSERT INTO order_item (id, customer_order_id, item_id, quantity)
VALUES
    (1, 1, 4, 1),
    (2, 2, 2, 1),
    (3, 3, 3, 1),
    (4, 4, 1, 1);

INSERT INTO payment (id, customer_order_id, payment_method, payment_status)
VALUES
    (1, 1, 'Кредитная карта', 'Оплачено'),
    (2, 2, 'Наличные', 'Оплачено'),
    (3, 3, 'Банковская перевод', 'Оплачено'),
    (4, 4, 'Дебетовая карта', 'Оплачено');

