"""
Цель:
Создать скрипт, который автоматически определяет Тип товара из доступных вариантов в
дереве категорий на основе данных, предоставленных поставщиком.
Список товаров к которым надо определить тип товара указан в файле Список товаров.
Ваш алгоритм должен определять тот же тип товара,
что указан в этом же файле в колонке Тип товара.

Данные:
Список товаров.xlsx - содержит данные с колонками:

Наименование - название товара;
Тип товара - тип товара (соответствует колонке Тип товара из файла Дерево категорий.xlsx), который на данный момент указан на площадке и который является значением для оценки ваших результатов.
Дерево категорий.xlsx - содержит иерархию категорий товаров в формате:


Главная категория - главная категория;
Дочерняя категория - подкатегория;
Тип товара - тип товара который вам и надо определить для каждого товара.
Данные поставщика.xlsx - содержит все доступные данные о товарах от поставщика.

Результат:
Скрипт должен определить тип хотя бы для одного типа товара, используя данные из файла
Данные поставщика.xlsx и соответствие типов из дерева категорий
"""
import pandas as pd
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# 1. Загрузка данных
df_products = pd.read_excel('Список товаров.xlsx')
df_categories = pd.read_excel('Дерево категорий.xlsx')
df_supplier = pd.read_excel('Данные поставщика.xlsx')

# print(df_products.head()) openpyxl

# 2. Предварительная обработка данных
def clean_text(text):
    if isinstance(text, str):
        # Приведение к нижнему регистру и удаление лишних пробелов
        text = text.lower().strip()
        # Удаление специальных символов
        text = re.sub(r'[^\w\s]', ' ', text)
        # Удаление множественных пробелов
        text = re.sub(r'\s+', ' ', text)
    return text


# 3. Создание расширенного словаря категорий
category_dict = {}
for _, row in df_categories.iterrows():
    main_cat = clean_text(row['Главная категория'])
    sub_cat = clean_text(row['Дочерняя категория'])
    product_type = row['Тип товара']

    # Добавляем полные названия категорий
    category_dict[main_cat] = product_type
    category_dict[sub_cat] = product_type

    # Добавляем отдельные слова из названий категорий
    for word in main_cat.split() + sub_cat.split():
        if len(word) > 3:  # Игнорируем слишком короткие слова
            category_dict[word] = product_type


# 4. Функция определения типа товара
def determine_product_type(product_name):
    product_name = clean_text(product_name)

    # 1. Прямое совпадение
    for category, product_type in category_dict.items():
        if category in product_name:
            return product_type

    # 2. Нечеткое сопоставление
    best_match = None
    highest_ratio = 0

    for category, product_type in category_dict.items():
        ratio = fuzz.partial_ratio(product_name, category)
        if ratio > highest_ratio and ratio > 80:  # Порог схожести
            highest_ratio = ratio
            best_match = product_type

    if best_match:
        return best_match

    # 3. Поиск по ключевым словам
    words = product_name.split()
    for word in words:
        if word in category_dict and len(word) > 3:
            return category_dict[word]

    return "Не определен"


# 5. Применение функции и анализ результатов
df_products['Определенный тип'] = df_products['Наименование'].apply(determine_product_type)
df_products['Успешно определен'] = df_products['Определенный тип'] == df_products['Тип товара']

# 6. Вывод результатов
success_rate = df_products['Успешно определен'].mean() * 100
print(f"Процент успешно определенных типов товаров: {success_rate:.2f}%")

# 7. Анализ неопределенных товаров
unidentified = df_products[df_products['Определенный тип'] == "Не определен"]
if not unidentified.empty:
    print("\nТовары, для которых тип не был определен:")
    print(unidentified[['Наименование', 'Тип товара']])

# 8. Анализ неправильно определенных товаров
incorrect = df_products[
    (df_products['Определенный тип'] != df_products['Тип товара']) &
    (df_products['Определенный тип'] != "Не определен")
    ]
if not incorrect.empty:
    print("\nНеправильно определенные товары:")
    print(incorrect[['Наименование', 'Тип товара', 'Определенный тип']])

# 9. Сохранение результатов
df_products.to_excel('Результаты_классификации.xlsx', index=False)





