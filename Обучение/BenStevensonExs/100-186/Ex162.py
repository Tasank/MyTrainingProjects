"""
Упражнение 162. Книги без буквы E.
Напишите программу, которая будет считывать список слов из файла и собирать статистику о том,
в каком проценте слов используется каждая буква алфавита.
Выведите результат для всех 26 букв английского алфавита и отдельно отметьте букву,
которая встречалась в словах наиболее редко.
В вашей программе должны игнорироваться знаки препинания и регистр символов.
"""
import string

# Список знаков препинания
punctuation = set(string.punctuation)


# Функция для обработки файла и создания словаря с частотой встречаемости букв
def procedure_chars_dict_if_file(filename):
    chars_dict = {char: 0 for char in string.ascii_lowercase}  # Инициализируем словарь для всех букв алфавита
    try:
        with open(filename, 'r') as readfile:
            text = readfile.read().lower()  # Приводим текст к нижнему регистру
            for char in text:
                if char not in punctuation and char.isalpha():
                    chars_dict[char] += 1  # Обновляем счётчик для каждой буквы
        return chars_dict
    except FileNotFoundError:
        print('Не удаётся открыть файл.')
        return None


# Главная функция для вывода статистики
def main(chars_dict):
    if chars_dict is None:
        return
    print('Статистика встречаемых букв в файле: ')
    for key, value in chars_dict.items():
        print(f'{key} - {value}')

    # Ищем букву с минимальной частотой, ниже объяснение
    min_char_key = min(chars_dict, key=chars_dict.get)
    print('Буква, которая встречалась в словах наиболее редко: ', min_char_key)


# Имя файла
filename = 'Ex162.txt'

# Запуск программы
chars_dict = procedure_chars_dict_if_file(filename)
main(chars_dict)

# Объяснение строки min_char_key = min(chars_dict, key=chars_dict.get)
# (key=chars_dict.get):
# - Аргумент key в функции min позволяет указать функцию, которая будет применяться к каждому элементу
# итерируемого объекта. (в данном случае, к каждому ключу словаря)
# (chars_dict.get) — это метод словаря, который возвращает значение для указанного ключа.
# Например, chars_dict.get('a') вернет частоту встречаемости буквы 'a' в тексте.
# - Таким образом, min(chars_dict, key=chars_dict.get) ищет минимальное значение,
# но вместо сравнения самих ключей (букв), оно сравнивает значения, возвращаемые chars_dict.get.