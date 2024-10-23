# pip install psycopg2-binary
import os
import psycopg2
from psycopg2 import sql


# Класс для работы с базой данных
class DatabaseHandler:
    # Устанавливаем значения переменных окружения
    os.environ['FSTR_DB_HOST'] = 'localhost'
    os.environ['FSTR_DB_PORT'] = '5432'
    os.environ['FSTR_DB_LOGIN'] = 'postgres'
    os.environ['FSTR_DB_PASS'] = '1234'

    def __init__(self):
        # Получаем параметры соединения из переменных окружения
        self.host = os.getenv('FSTR_DB_HOST')
        self.port = os.getenv('FSTR_DB_PORT')
        self.user = os.getenv('FSTR_DB_LOGIN')
        self.password = os.getenv('FSTR_DB_PASS')
        self.database = 'Pereval'  # Название базы данных
        # Создаем соединение с базой данных
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.conn.autocommit = True

    # Метод для добавления координат
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

    # Метод для добавления пользователя
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

    # Метод для добавления перевала
    def add_pereval(self, beauty_title, title, other_titles, connect, add_time, user_id, coord_id, level_winter,
                    level_summer, level_autumn, level_spring, status):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("""
                INSERT INTO pereval_added (beauty_title, title, other_titles, connect, add_time, user_id, coord_id, level_winter, level_summer, level_autumn, level_spring, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)
                RETURNING id;
                """)
                cursor.execute(query, (
                    beauty_title, title, other_titles, connect, add_time, user_id, coord_id, level_winter, level_summer,
                    level_autumn, level_spring))
                pereval_id = cursor.fetchone()[0]
                return pereval_id
        except psycopg2.Error as e:
            print(f"Ошибка при добавлении перевала: {e}")
            return None

    # Метод для добавления изображения
    def add_image(self, image_data, image_title, pereval_id):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("""
                INSERT INTO images (data, title, pereval_id)
                VALUES (%s, %s, %s)
                RETURNING id;
                """)
                cursor.execute(query, (image_data, image_title, pereval_id))
                image_id = cursor.fetchone()[0]
                return image_id
        except psycopg2.Error as e:
            print(f"Ошибка при добавлении изображения: {e}")
            return None

    # Метод для проверки существования пользователя
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
        except psycopg2.Error as e:
            print(f"Ошибка при проверке существования пользователя: {e}")
            return False

    # Метод для получения перевала по его ID
    def get_pereval_by_id(self, pereval_id):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("SELECT * FROM pereval_added WHERE id = %s;")
                cursor.execute(query, (pereval_id,))
                record = cursor.fetchone()
                return record
        except Exception as e:
            print(f"Ошибка при получении перевала: {e}")
            return None

    # Метод для обновления перевала
    def update_pereval(self, pereval_id, data):
        try:
            with self.conn.cursor() as cursor:
                # Проверяем статус, чтобы разрешить редактирование только если статус new
                cursor.execute("SELECT status FROM pereval_added WHERE id = %s;", (pereval_id,))
                status = cursor.fetchone()[0]
                if status != 'new':
                    return {'state': 0, 'message': 'Редактирование возможно только для записей со статусом new'}

                # Подготовка запроса на обновление
                update_query = sql.SQL("""
                    UPDATE pereval_added
                    SET beauty_title = %s, title = %s, other_titles = %s, connect = %s, add_time = %s,
                        level_winter = %s, level_summer = %s, level_autumn = %s, level_spring = %s
                    WHERE id = %s
                """)
                cursor.execute(update_query, (
                    data.get('beauty_title'),
                    data.get('title'),
                    data.get('other_titles', ""),
                    data.get('connect', ""),
                    data.get('add_time'),
                    data.get('level', {}).get('winter'),
                    data.get('level', {}).get('summer'),
                    data.get('level', {}).get('autumn'),
                    data.get('level', {}).get('spring'),
                    pereval_id
                ))
                return {'state': 1, 'message': 'Запись успешно обновлена'}
        except Exception as e:
            print(f"Ошибка при обновлении перевала: {e}")
            return {'state': 0, 'message': f"Ошибка при обновлении: {e}"}

    # Метод для получения перевалов по email пользователя
    def get_submissions_by_user_email(self, email):
        try:
            with self.conn.cursor() as cursor:
                query = sql.SQL("""
                    SELECT * FROM pereval_added
                    WHERE user_id = (SELECT id FROM users WHERE email = %s)
                    """)
                cursor.execute(query, (email,))
                records = cursor.fetchall()
                return records
        except Exception as e:
            print(f"Ошибка при получении данных пользователя: {e}")
            return []

    def close(self):
        self.conn.close()


# Пример использования
if __name__ == "__main__":

    db_handler = DatabaseHandler()
    # узнать существует ли пользователь
    email = '1example@example.com'
    if not db_handler.check_user_exists(email):
        # Пример добавления нового пользователя
        user_id = db_handler.add_user(email, 'Иван', 'Иванов', 'Иванович', '+7 123 456 78 90')
        # Если пользователь успешно добавлен
        if user_id:
            # То добавляем координаты
            coord_id = db_handler.add_coord(45.0, 30.0, 1000)
            # Если координаты успешно добавлены
            if coord_id:
                # То добавляем перевал
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
                    level_spring="",
                    status="new"
                )

                if pereval_id:
                    print(f"Перевал успешно добавлен: {pereval_id}")
    else:
        print(f"Пользователь с электронной почтой {email} уже существует.")

    db_handler.close()
