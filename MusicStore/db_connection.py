import psycopg2

class DatabaseManager:
    def __init__(self, host, port, dbname, user, password):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        self.connection.autocommit = True

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description:  # Если есть результаты
                return cursor.fetchall()  # Возвращаем все записи
            return cursor.rowcount  # Если это команда изменения

    def fetch_all(self, query, params=None):
        return self.execute_query(query, params)  # Используем execute_query

    def fetch_one(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()  # Возвращаем одну запись

    def close(self):
        self.connection.close()
