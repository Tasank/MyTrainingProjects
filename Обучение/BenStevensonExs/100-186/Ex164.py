"""
Упражнение 164. Универсальные имена.
Напишите программу, которая будет выводить на экран имена, использованные
для мальчиков и девочек в указанном пользователем году. Если в этом году универсальных имен не было,
нужно известить об этом пользователя. Кроме того, если за указанный пользователем год не было данных по именам,
выведите соответствующее сообщение об ошибке. Дополнительные детали по хранению имен в файлах – в упражнении 163
"""
import os

# Создаем множество для хранения универсальных имен
set_name_universal = set()

# Путь к папке с файлами, расположенной рядом с текущим скриптом
data_path = os.path.join(os.path.dirname(__file__), 'names')

# Ввод диапазона годов пользователем
first_year = int(input('Введите первый год: '))
second_year = int(input('Введите последний год: '))

# Обработка файлов за каждый год в указанном диапазоне
for year in range(first_year, second_year + 1):
    file_name = f'yob{year}.txt'
    file_path = os.path.join(data_path, file_name)

    # Проверка существования файла
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as read_file:
                # Инициализируем словарь для хранения имен и их полов
                universal_names = {}

                for line in read_file:
                    name, gender, _ = line.strip().split(',')
                    # Если имя уже есть в словаре, добавляем пол в множество
                    if name in universal_names:
                        universal_names[name].add(gender)
                    else:
                        universal_names[name] = {gender}

                # Добавляем имена, которые использовались для обоих полов, в итоговое множество
                for name, genders in universal_names.items():
                    if len(genders) > 1:
                        set_name_universal.add(name)

        except Exception as e:
            print(f'Не удалось открыть файл {file_name}: {e}')

    else:
        print(f'Данные за {year} год отсутствуют.')

# Преобразование множества в список (если требуется)
name_list = list(set_name_universal)

# Вывод результатов
if set_name_universal:
    print("Универсальные имена в указанном промежутке:", name_list)
else:
    print('В указанном промежутке универсальных имен не было.')