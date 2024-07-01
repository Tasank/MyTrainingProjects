"""
Упражнение 163. Популярные детские имена.
Напишите программу, которая будет считывать по одному все файлы из набора данных и выделять имена,
которые были лидерами по частоте использования как минимум в одном году.
На выходе должно получиться два списка: в одном из них будут присутствовать наиболее популярные имена для мальчиков,
во втором – для девочек. При этом списки не должны содержать повторяющиеся имена.
"""
import os

# Данные имён можно скачать с официального SSA (например, по адресу https://www.ssa.gov/oact/babynames/limits.html)
# Уникальные множества самых популярных имён
set_boy_name_leaders = set()
set_girl_name_leaders = set()

# Путь к папке с файлами, расположенный рядом с текущим скриптом
data_patch = os.path.join(os.path.dirname(__file__), 'names')

# Обработка файлов
for year in range(1880, 2023):
    file_name = f'yob{year}.txt'
    file_patch = os.path.join(data_patch, file_name)

    #  Проверка существования файла
    if os.path.exists(file_patch):
        try:
            with open(file_patch, 'r') as read_file:
                # Инициализируем счётчики
                boys_counter = {}
                girls_counter = {}

                for line in read_file:
                    name, gender, state = line.strip().split(',')
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

                if boys_counter:
                    boys_name_leader = max(boys_counter, key=boys_counter.get)
                    set_boy_name_leaders.add(boys_name_leader)
                if girls_counter:
                    girls_name_leader = max(girls_counter, key=girls_counter.get)
                    set_girl_name_leaders.add(girls_name_leader)

        except:
            print('Не удалось открыть файл')

# Преобразование множеств в списки
boys_leaders_list = list(set_boy_name_leaders)
girls_leaders_list = list(set_girl_name_leaders)

# Вывод результатов
print("Наиболее популярные американские имена мальчиков:", boys_leaders_list)
print("Наиболее популярные американские имена девочек:", girls_leaders_list)