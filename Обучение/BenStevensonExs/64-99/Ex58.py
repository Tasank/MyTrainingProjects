"""
Упражнение 58. Високосный год?
Напишите программу, запрашивающую год у пользователя и выводящую сообщение о том, високосный ли он.
"""

def check_year(year):
    # Переменная для определения года
    total = False
    # Проходим по условиям
    if year % 400 == 0:
        total = True
    elif (year % 400) % 4 == 0:
        total = True
    return total

def main():
    # Ввод года пользователем
    year = int(input('Введите интересующий год: '))
    # Если total = False, то год не високосный
    if check_year(year):
        print(f'{year} год является високосным.')
    else:
        print(f'{year} год не является високосным.')

if __name__ == '__main__':
    main()