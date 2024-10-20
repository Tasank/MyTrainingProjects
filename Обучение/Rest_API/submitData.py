# pip install psycopg2-binary
import os
import psycopg2
from psycopg2 import sql

# Класс для работы с базой данных
class DatabaseHandler:

    def __init__(self):
        # Получаем параметры соединения из переменных окружения
        self.host = os.getenv('FSTR_DB_HOST')
        self.port = os.getenv('FSTR_DB_PORT')
        self.user = os.getenv('FSTR_DB_LOGIN')
        self.password = os.getenv('FSTR_DB_PASS')
        self.database = 'Pereval'  # Название вашей базы данных
        # Создаем соединение с базой данных
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.conn.autocommit = True

    def add_coord(self, latitude, longitude, height):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("""
                INSERT INTO coords (latitude, longitude, height)
                VALUES (%s, %s, %s)
                RETURNING id;
                """)
                cursor.execute(query, (latitude, longitude, height))
                coord_id = cursor.fetchone()[0]
                return coord_id
        except Exception as e:
            print(f"Ошибка при добавлении координат: {e}")
            return None

    def add_user(self, email, fam, name, otc, phone):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("""
                INSERT INTO users (email, fam, name, otc, phone)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """)
                cursor.execute(query, (email, fam, name, otc, phone))
                user_id = cursor.fetchone()[0]
                return user_id
        except Exception as e:
            print(f"Ошибка при добавлении пользователя: {e}")
            return None
    def add_pereval(self, beauty_title, title, other_titles, connect, add_time, user_id, coord_id, level_winter, level_summer, level_autumn, level_spring):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("""
                INSERT INTO pereval_added (beauty_title, title, other_titles, connect, add_time, user_id, coord_id, level_winter, level_summer, level_autumn, level_spring)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id;
                """)
                cursor.execute(query, (beauty_title, title, other_titles, connect, add_time, user_id, coord_id, level_winter, level_summer, level_autumn, level_spring))
                pereval_id = cursor.fetchone()[0]
                return pereval_id
        except Exception as e:
            print(f"Ошибка при добавлении перевала: {e}")
            return None

    def check_user_exists(self, email):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("""
                SELECT * FROM users
                WHERE email = %s;
                """)
                cursor.execute(query, (email,))
                user = cursor.fetchone()
                return user is not None
        except Exception as e:
            print(f"Ошибка при проверке существования пользователя: {e}")
            return False

    def close(self):
        self.conn.close()

# добавить новую запись в таблицу users с id равным 1:


# Пример использования
if __name__ == "__main__":
    # Устанавливаем значения переменных окружения
    os.environ['FSTR_DB_HOST'] = 'localhost'
    os.environ['FSTR_DB_PORT'] = '5432'
    os.environ['FSTR_DB_LOGIN'] = 'postgres'
    os.environ['FSTR_DB_PASS'] = '1234'

    db_handler = DatabaseHandler()

    email = 'example@example.com'
    if not db_handler.check_user_exists(email):
        user_id = db_handler.add_user(email, 'Иван', 'Иванов', 'Иванович', '+7 123 456 78 90')
        if user_id:
            coord_id = db_handler.add_coord(45.0, 30.0, 1000)
            if coord_id:
                # Пример добавления нового перевала
                pereval_id = db_handler.add_pereval(
                    beauty_title="пер. ",
                    title="Пхия",
                    other_titles="Триев",
                    connect="",
                    add_time="2021-09-22 13:18:13",
                    user_id=user_id,
                    coord_id=coord_id,
                    level_winter="",
                    level_summer="1А",
                    level_autumn="1А",
                    level_spring=""
                )

                if pereval_id:
                    print(f"Перевал успешно добавлен: {pereval_id}")
    else:
        print(f"Пользователь с электронной почтой {email} уже существует.")

db_handler.close()