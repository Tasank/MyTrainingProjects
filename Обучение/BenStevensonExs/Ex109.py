"""
Упражнение 109. Магические даты.
Напишите функцию, определяющую, является ли введенная дата магической. Используйте написанную функцию в главной
программе для отображения всех магических дат в 21 веке. Возможно, вам пригодится здесь функция,
разработанная в упражнении 106.
"""
from Ex106 import check_day
print('Отображения всех магических дат в XXI веке.')
def magic(day, month, year):
    # Представление кода в 2 цифрах
    if day * month == year % 100:
        return True
    return False

def ask():
    for year in range(2000, 2100):
        for month in range(1, 13):
            for day in range(1, check_day(month, year) + 1):
                if magic(day, month, year):
                    print(' %02d|%02d|%04d - Магическая дата.' % (day, month, year))


ask()