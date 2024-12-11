"""
Отправить запрос к любому доступному API (например, сервис погоды, публичный API, JSON-ресурс).
Вывести результат в структурированном виде (например, таблица, список или хотя бы обычный print c f-строками).
"""
import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

# Загрузка из .енв
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
KEY_API = os.getenv('KEY_API')

def get_weather(api_key, city):
    base_url = "http://api.weatherapi.com/v1/current.json"

    # Параметры запроса
    params = {
        'key': api_key,
        'q': city,
        'aqi': 'no'  # Не включаем данные о качестве воздуха
    }

    try:
        # Отправляем GET запрос
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Проверка на ошибки

        # Получаем данные в формате JSON
        data = response.json()

        # Извлекаем нужные данные
        weather_data = {
            'Город': data['location']['name'],
            'Страна': data['location']['country'],
            'Местное время': data['location']['localtime'],
            'Температура °C': data['current']['temp_c'],
            'Ощущается как °C': data['current']['feelslike_c'],
            'Состояние': data['current']['condition']['text'],
            'Влажность %': data['current']['humidity'],
            'Скорость ветра км/ч': data['current']['wind_kph']
        }

        # Создаем DataFrame
        df = pd.DataFrame([weather_data])

        return df

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None


api_key = KEY_API

cities = ["Moscow", "London", "New York", "Tokyo", "Paris"]

# пустой DataFrame для хранения всех результатов
all_weather_data = pd.DataFrame()

# Получить данные для каждого города
for city in cities:
    weather_df = get_weather(api_key, city)
    if weather_df is not None:
        all_weather_data = pd.concat([all_weather_data, weather_df], ignore_index=True)

# Вывод результатов
print("\nТекущая погода в разных городах:")
print("=" * 100)
print(all_weather_data.to_string(index=False))

# Сохраняем результаты в Excel файл
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"weather_data_{timestamp}.xlsx"
all_weather_data.to_excel(filename, index=False)
print(f"\nРезультаты сохранены в файл: {filename}")
