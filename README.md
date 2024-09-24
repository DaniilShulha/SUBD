## Библиотека
### Функциональные требования
#### Общие требования

1. Регистрация пользователя
2. Авторизация
3. Просмотр, заказ и управление блюдами
4. Оформление заказа на блюда
5. Выдача счетов и управление платежами
6. Система ролей (клиент, администратор, менеджер)
7. Возможность оставить отзыв о блюдах
8. Журналирование всех действий пользователей


#### Клиент

1. Авторизация и регистрация
2. CRUD отзывов о блюдах
3. CRUD заказов(оформить заказ, просмотр заказов, возврат заказа)
4. Оплата заказов и управление платежами
5. Изменение, удаление профиля

#### Менеджер

1. Авторизация(регистрация по умолчанию должен быть в системе)
2. CRUD заказов(изменение статусов, удаление заказов)
3. Управление меню и блюдами

#### Администратор системы

CRUD со всеми сущностями системы:
1. Пользователь (клиент, менеджер, администратор)
2. Блюдо
3. Категория блюд
4. Заказ
5. Стол
6. Оплата
7. Отзывы
8. Журнал действий
9. Резервирование столов
10. Кухня

#### Перечень сущностей

### 1. users - пользователь

#### Поля:
- first_name (имя) - varchar
- last_name (фамилия) - varchar
- password_hash (захешированный пароль) - varchar
- email (почта) - varchar
- created_at (дата создания) TIMESTAMP DEFAULT NOW()
- user_role (роль пользователя) - Enum('CLIENT', 'MANAGER', 'ADMINISTRATOR')

### 2. dishes - блюдо

#### Поля:
- title (название) - varchar
- description (описание) - text
- price (цена) - decimal
- category_id (идентификатор категории) - int, many-to-one relationship

#### Связи:
- many-to-one с моделью categories

### 3. categoories - категории

#### Поля:
- name (название) - varchar

### 4. orders - заказ

#### Поля:
- user_id (идентификатор пользователя) - int, many-to-one relationship
- status (статус) - ENUM('NEW', 'IN_PROCESS', 'COMPLETED', 'CANCELLED')
- total_price (общая сумма) - decimal
- created_at (дата создания) - TIMESTAMP DEFAULT NOW()

#### Связи:
- many-to-one с моделью users

### 5. tables - столы

#### Поля:
- number (номер стола) - int
- capacity (вместимость) - int 
- is_reserved (занят или нет) - boolean

### 6. payments - платежи

#### Поля:
- order_id (идентификатор заказа) - int, many-to-one relationship
- amount (сумма) - decimal
- payment_date (дата платежа) - TIMESTAMP

#### Связи:
- many-to-one с моделью orders

### 7. feedbacks - отзывы

#### Поля:
- user_id (идентификатор пользователя) - int, many-to-one relationship
- dish_id (идентификатор блюда) - int, many-to-one relationship
- description (описание) - text
- rating (оценка) - int

#### Связи:
- many-to-one с моделью users
- many-to-one с моделью dishes

### 8. action_logs - журнал действий

#### Поля:
- user_id (идентификатор пользователя) - int, many-to-one relationship
- action (действие) - varchar
- timestamp (время действия) - TIMESTAMP

#### Связи:
- many-to-one с моделью users

### 9. reservations - резервирование

#### Поля:
- table_id (идентификатор стола) - int, many-to-one relationship
- user_id (идентификатор пользователя) - int, many-to-one relationship
- reservation_time (время резервирования) - TIMESTAMP

#### Связи:
- many-to-one с моделью tables
- many-to-one с моделью users

### 10. kitchens - кухня

#### Поля:
- name (название) - varchar
