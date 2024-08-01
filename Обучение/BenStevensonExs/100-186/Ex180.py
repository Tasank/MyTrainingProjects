"""
Упражнение 180. Редакционное расстояние.
Напишите рекурсивную функцию, вычисляющую редакционное расстояние между двумя строками по следующему алгоритму.
"""


def editorial_distance(s, t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    cost = 0
    if s[-1] != t[-1]:
        cost = 1

    # Рекурсивные вычисления
    d1 = editorial_distance(s[:-1], t) + 1
    d2 = editorial_distance(s, t[:-1]) + 1
    d3 = editorial_distance(s[:-1], t[:-1]) + cost

    # Возвращаем минимальное значение среди d1, d2 и d3
    return min(d1, d2, d3)


# Запрос вводных
s = input('Введите первое слово: ')
t = input('Введите второе слово: ')

print(editorial_distance(s, t))

print(editorial_distance(s, t))
