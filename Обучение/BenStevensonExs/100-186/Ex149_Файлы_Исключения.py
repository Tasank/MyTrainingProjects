"""
Упражнение 149. Отображаем начало файла.
В операционных системах на базе Unix обычно присутствует утилита с названием head.
Она выводит первые десять строк содержимого файла, имя которого передается в качестве аргумента командной строки.
Напишите программу на Python, имитирующую поведение этой утилиты. Если файла, указанного пользователем,
не существует, или не задан аргумент командной строки, необходимо вывести соответствующее сообщение об ошибке.
"""
# content = 'exemple.txt'
def read_ten_str_file(content):
    try:
        read_file = open(content, 'r')
        for i in range(10):
            line = read_file.readline()
            if line:
                print(line)
            else:
                break
        read_file.close()

    except FileNotFoundError:
        print(f'Файл {content} не найден')

content = input('Введите имя файла: ')

read_ten_str_file(content)