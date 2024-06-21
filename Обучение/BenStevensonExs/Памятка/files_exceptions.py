"""Функция open принимает два аргумента. Первый из них указывает имя файла,
который необходимо открыть. Второй аргумент также является текстовым и характеризует режим доступа
(access mode) к файлу. Мы будем работать с тремя режимами доступа к файлу:
на чтение (r), запись (w) и добавление (a)."""
# открытие файлов
#inf = open("input.txt", "r")
ex_file = 'exemple.txt'

import sys

# Открытие файла для чтения
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Содержимое файла {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")

# Открытие файла для записи (добавление в конец файла)
def append_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
        print(f"Записано в файл {filename}")

# Открытие файла для записи (перезапись файла)
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print(f"Записано в файл {filename}")

# Получение аргументов командной строки
def get_command_line_arguments():
    arguments = sys.argv[1:]
    print("Аргументы командной строки:")
    for arg in arguments:
        print(arg)

# Пример использования функций
def main():
    # Чтение из файла
    read_file(ex_file)

    # Запись в файл
    append_file("output.txt", "Привет, мир!")
    append_file(ex_file, "Привет, мир!")
    write_file("output.txt", "Это новая строка!")

    # Чтение из файла
    read_file(ex_file)
    read_file("output.txt")

    # Аргументы командной строки
    get_command_line_arguments()

if __name__ == "__main__":
    main()
