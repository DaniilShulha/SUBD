## Система управления заказами в ресторане
### Функциональные требования
#### Общие требования

1. Регистрация пользователя
2. Авторизация
3. Просмотр, заказ и управление музыкальными инструментами
4. Оформление заказов
5. Выдача счетов и управление платежами
6. Система ролей (клиент, администратор, менеджер)
7. Возможность оставить отзыв на инструмент
8. Журналирование всех действий пользователей


#### Клиент

1. Авторизация и регистрация
2. CRUD отзывов об инструментах
3. CRUD заказов (оформление заказа, просмотр заказов, возврат)
4. Оплата заказов и управление платежами
5. Изменение и удаление профиля

#### Менеджер

1. Авторизация (регистрация по умолчанию не требуется)
2. CRUD заказов (изменение статусов, удаление заказов)
3. Управление инструментами и категориями товаров

#### Администратор системы

CRUD со всеми сущностями системы:
1. Пользователь (клиент, менеджер, администратор)
2. Музыкальные инструменты
3. Категории товаров
4. Заказы
5. Платежи
6. Отзывы
7. Журнал действий

#### Перечень сущностей

### 1. customer - пользователь

#### Поля:
- id (айди) - int
- customer_name (имя) - varchar
- email (почта) - varchar
- password (пароль) - varchar
- country_id (идентификатор страны) - int, many-to-one relationship

#### Связи:
- many-to-one с моделью country

### 2. item - товар

#### Поля:
- id (айди) - int
- instrument_id (идентификатор инструмента) - int, many-to-one relationship
- serial_number (серийный номер) - varchar
- description (описание) - text
- year_of_production (год выпуска) - int
- country_id (идентификатор страны) - int, many-to-one relationship
- price (цена) - decimal

#### Связи:
- many-to-one с моделью instrument
- many-to-one с моделью order_item

### 3. categoory - категории

#### Поля:
- id (айди) - int
- category_name (название категории) - varchar

#### Связи:
- one-to-many с моделью instrument

### 4. instrument - музыкальный инструмент

#### Поля:
- id (айди) - int
- instrument_name (название инструмента) - varchar
- manufacturer_id (идентификатор производителя) - int, many-to-one relationship
- category_id (идентификатор категории) - int, many-to-one relationship
- description (описание) - text

#### Связи:
- many-to-one с моделью category
- many-to-one с моделью manufacturer

### 5. manufacturer - производитель

#### Поля:
- id (айди) - int
- name (название производителя) - varchar
- country_id (идентификатор страны) - int, many-to-one relationship

#### Связи:
- many-to-one с моделью country

### 6. country - страна

#### Поля:
- id (айди) - int
- country_name (название страны) - varchar

### 7. customer_order - заказ

#### Поля:
- id (айди) - int
- customer_id (идентификатор клиента) - int, many-to-one relationship
- delivery_address (адрес доставки) - varchar
- order_time (время заказа) - TIMESTAMP
- preferred_delivery_time (предпочтительное время доставки) - TIMESTAMP
- order_status_id (идентификатор статуса заказа) - int, many-to-one relationship
- time_paid (время оплаты) - TIMESTAMP, nullable
- time_canceled (время отмены) - TIMESTAMP, nullable
- time_completed (время завершения) - TIMESTAMP, nullable
- total_price (общая сумма) - decimal
- discount (скидка) - decimal
- active (активность) - boolean

#### Связи:
- many-to-one с моделью customer
- many-to-one с моделью order_status

### 8. order_item - элементы заказа

#### Поля:
- id (айди) - int
- customer_order_id (идентификатор заказа) - int, many-to-one relationship
- item_id (идентификатор товара) - int, many-to-one relationship
- price (цена) - decimal

#### Связи:
- many-to-one с моделью item
- many-to-one с моделью customer_order

### 9. payment - платеж

#### Поля:
- id (айди) - int
- sorder_id (идентификатор заказа) - int, many-to-one relationship
- payment_method (способ оплаты) - varchar
- payment_status (статус оплаты) - varchar
- payment_date (дата оплаты) - TIMESTAMP

#### Связи:
- many-to-one с моделью customer_orders


### 10. review - отзыв

#### Поля:
- id (айди) - int
- customer_id (идентификатор клиента) - int, many-to-one relationship
- instrument_id (идентификатор инструмента) - int, many-to-one relationship
- description (описание) - text
- rating (оценка) - int

#### Связи:
- many-to-one с моделью customers
- many-to-one с моделью instruments

