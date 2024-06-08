"""
Упражнение 133. Содержит ли список подмножество элементов?
В рамках данного упражнения вам необходимо написать функцию isSublist, определяющую, является ли один список
подсписком другого. На вход функции должны поступать два списка – larger и smaller. Функция должна возвращать значение
True только в том случае, если список smaller является подсписком списка larger.
Напишите также основную программу для демонстрации работы функции.
"""

def isSublist(larger, smaller):
    if not smaller:
        return True
    elif smaller == larger:
        return True
    for i in range(len(larger) - len(smaller) + 1):
        # Сравниваем срез с larger с подсписком smaller
        if larger[i:i + len(smaller)] == smaller:
            return True
    return False


def main():
    larger = list(map(int, input('Введите список чисел через пробел: ').split()))
    smaller = list(map(int, input('Введите подсписок чисел через пробел: ').split()))

    if isSublist(larger, smaller):
        print('Этот подсписок является частью списка.')
    else:
        print('Этот подсписок не является частью списка.')

if __name__ == '__main__':
    main()