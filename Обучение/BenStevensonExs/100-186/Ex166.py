"""
Упражнение 166. Имена без повторов.
Продолжаем использовать базу имен из упражнения 163. Проходя по файлам,
выберите имена без дублирования отдельно для мальчиков и для девочек и выведите их на экран.
Разумеется, повторяющихся имен в этих списках быть не должно.
"""
## Примечание! Код учитывает "имена без повторов" для отдельно каждого года,
# а не только "одно имя за весь диапазон лет".
# Почему так? Потому как задача не поясняет что именно нужно. За весь период или каждый год.
# Из-за этого вывод такой большой.

import os

# Уникальные множества самых популярных имён
set_boy_name = set()
set_girl_name = set()

# Путь к папке с файлами, расположенный рядом с текущим скриптом
data_path = os.path.join(os.path.dirname(__file__), 'names')  # Исправлено __file__

# Обработка файлов
for year in range(2020, 2023):
    file_name = f'yob{year}.txt'
    file_path = os.path.join(data_path, file_name)

    # Проверка существования файла
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as read_file:
                boys_counter = {}
                girls_counter = {}

                for line in read_file:
                    name, gender, _ = line.strip().split(',')
                    # Подсчет имен
                    if gender == 'M':
                        if name in boys_counter:
                            boys_counter[name] += 1
                        else:
                            boys_counter[name] = 1
                    elif gender == 'F':
                        if name in girls_counter:
                            girls_counter[name] += 1
                        else:
                            girls_counter[name] = 1

                for name, count in boys_counter.items():
                    if count == 1:
                        set_boy_name.add(name)
                for name, count in girls_counter.items():
                    if count == 1:
                        set_girl_name.add(name)

        except Exception as e:
            print(f'Не удалось открыть файл {file_name}: {e}')
    else:
        print(f'Файл {file_name} не найден.')

# Преобразование множеств в списки
boys_list = list(set_boy_name)
girls_list = list(set_girl_name)

# Вывод результатов
print("Имена без повторов мальчиков:", boys_list)
print("Имена без повторов девочек:", girls_list)

"""
Вот решение за весь период.
defaultdict — это подкласс стандартного словаря (dict) из модуля collections, который предоставляет значение 
по умолчанию для несуществующих ключей. 
Это позволяет избегать ошибок при обращении к несуществующим ключам и упрощает код.

Когда вы создаете defaultdict с аргументом int, это означает, что для каждого нового ключа, 
который еще не существует в словаре, будет автоматически создано значение типа int с начальным значением 0. 
Это особенно полезно для подсчета, так как вы можете сразу увеличивать значение, не проверяя наличие ключа.
"""
# import os
# from collections import defaultdict
#
# # Уникальные множества самых популярных имён
# boys_counter = defaultdict(int)
# girls_counter = defaultdict(int)
#
# # Путь к папке с файлами, расположенный рядом с текущим скриптом
# data_path = os.path.join(os.path.dirname(__file__), 'names')
#
# # Обработка файлов
# for year in range(2020, 2023):  # Диапазон лет с 2020 по 2022 включительно
#     file_name = f'yob{year}.txt'
#     file_path = os.path.join(data_path, file_name)
#
#     # Проверка существования файла
#     if os.path.exists(file_path):
#         try:
#             with open(file_path, 'r') as read_file:
#                 for line in read_file:
#                     name, gender, _ = line.strip().split(',')
#                     # Подсчет имен
#                     if gender == 'M':
#                         boys_counter[name] += 1
#                     elif gender == 'F':
#                         girls_counter[name] += 1
#
#         except Exception as e:
#             print(f'Не удалось открыть файл {file_name}: {e}')
#     else:
#         print(f'Файл {file_name} не найден.')
#
# # Фильтрация имен, которые встречаются только один раз за все годы
# unique_boys = [name for name, count in boys_counter.items() if count == 1]
# unique_girls = [name for name, count in girls_counter.items() if count == 1]
#
# # Вывод результатов
# print("Имена без повторов мальчиков:", unique_boys)
# print("Имена без повторов девочек:", unique_girls)
