"""
Упражнение 88. Медиана трех значений.
Напишите функцию, которая будет принимать на вход три числа в качестве параметров и возвращать их медиану.
В основной программе должен производиться запрос к пользователю на предмет ввода трех чисел,
а также вызов функции и отображение результата.
"""
# @param a - первое значение
# @param b - второе значение
# @param c - третье значение
# @return медиана чисел a, b и c
#
def median(a, b, c):
    if a < b and b < c or a > b and b > c:
        return b
    if b < a and  a < c or b > a and a > c:
        return a
    if c < a and b < c or c > a and b > c:
        return c

def alt_median(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

def main():
    x = float(input('Введите первое число: '))
    y = float(input('Введите второе число: '))
    z = float(input('Введите третье число: '))
    print("Медиана равна: ", median(x,y,z))
    print('Второй способ: ', alt_median(x,y,z))

main()
