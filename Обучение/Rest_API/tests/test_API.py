import pytest
import json
import requests

BASE_URL = "http://localhost:5000"  # Замените на адрес вашего API

def test_submit_data():
    data = {
        "beauty_title": "пер. ",
        "title": "Пхия",
        "other_titles": "Триев",
        "connect": "",
        "add_time": "2021-09-22 13:18:13",
        "user": {
            "email": "test10@example.com",
            "fam": "Иванов",
            "name": "Иван",
            "otc": "Иванович",
            "phone": "+7 123 456 78 92"
        },
        "coords": {
            "latitude": 45.0,
            "longitude": 30.0,
            "height": 1000
        },
        "level": {
            "winter": "1A",
            "summer": "1A",
            "autumn": "1A",
            "spring": "1A"
        },
        "images": []
    }

    response = requests.post(f"{BASE_URL}/submitData", json=data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_submit_data():
    response = requests.get(f"{BASE_URL}/submitData/5")  # Замените на правильный ID
    assert response.status_code == 200
    assert "data" in response.json()

def test_patch_submit_data():
    data = {
        "beauty_title": "новый заголовок",
        "title": "новое название",
        "add_time": "2024-10-23 13:00:00",
        "level": {
            "winter": "1B",
            "summer": "1A",
            "autumn": "1A",
            "spring": "1B"
        }
    }
    response = requests.patch(f"{BASE_URL}/submitData/5", json=data)  # Замените на правильный ID
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert response_json["message"] == "Запись успешно обновлена"

# def test_get_user_submissions():
#     response = requests.get(f"{BASE_URL}/submitData", params={'user__email': 'test3@example.com'})
#     assert response.status_code == 200
#     assert "data" in response.json()

