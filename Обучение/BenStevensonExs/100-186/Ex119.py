"""
Упражнение 119. Ниже и выше среднего.
Напишите программу, которая будет запрашивать у пользователя числа, пока он не пропустит ввод.
Сначала на экран должно быть выведено среднее значение введенного ряда чисел, после этого друг за другом необходимо
вывести список чисел ниже среднего, равных ему (если такие найдутся) и выше среднего.
Каждый список должен предваряться соответствующим заголовком.
"""
# Импортируем функцию возвращающую среднее значение данных
from statistics import median

def func():
    ask = input('Введите число: ')
    num_list = []

    zeros = []
    negatives = []
    positives = []

    while ask != '':
        num_list.append(int(ask))
        ask = input('Введите число (Enter для выхода): ')

    # Среднее значение
    medium_num = median(num_list)
    # Сортировка данных по их спискам
    for i in num_list:
        if i < medium_num:
            negatives.append(i)
        elif i > medium_num:
            positives.append(i)
        elif i == medium_num:
            zeros.append(i)

    # Сортировка списков
    negatives.sort()
    positives.sort()

    print('Среднее значение введённых данных: %.1f' % medium_num)
    print('Числа ниже среднего: ', negatives)
    print('Числа среднего значения: ', zeros)
    print('Числа выше среднего: ', positives)
func()