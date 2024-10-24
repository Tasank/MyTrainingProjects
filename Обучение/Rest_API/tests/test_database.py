import pytest
from Обучение.Rest_API.DatabaseHandler import DatabaseHandler


@pytest.fixture
def db_handler():
    handler = DatabaseHandler()
    yield handler
    handler.close()  # Закрытие соединения после тестов


def test_add_user(db_handler):
    email = "hopi@example.com"
    user_id = db_handler.add_user(email, "Иван", "Иванов", "Иванович", "+7 123 456 78 90")
    assert user_id is not None

    # Проверяем, что пользователь добавлен
    assert db_handler.check_user_exists(email)


def test_add_coord(db_handler):
    coord_id = db_handler.add_coord(45.0, 30.0, 1000)
    assert coord_id is not None


def test_add_pereval(db_handler):
    user_id = db_handler.add_user("hova@example.com", "Петр", "Петров", "Петрович", "+7 123 456 78 91")
    coord_id = db_handler.add_coord(45.0, 30.0, 1000)

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

    assert pereval_id is not None
