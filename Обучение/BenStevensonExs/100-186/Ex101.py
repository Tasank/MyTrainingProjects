"""
Упражнение 101. Случайный номерной знак.
Напишите функцию, которая будет генерировать случайный номерной знак.
При этом номера в старом и новом форматах должны создаваться примерно с одинаковой вероятностью.
В основной программе нужно сгенерировать и вывести на экран случайный номерной знак.
"""
from random import randint
def generate():
    old_new = randint(3, 4)
    mark = ''
    # генерируем номерной знак старого типа
    if old_new == 3:
        for i in range(old_new):
            mark += chr(randint(65, 90))
        for i in range(old_new):
            mark += str(randint(0, 9))
        print('Ваш случайный номерной знак - старого типа: ', mark)
    # генерируем номерной знак нового типа
    elif old_new == 4:
        for i in range(old_new):
            mark += str(randint(0, 9))
        for i in range(3):
            mark += chr(randint(65, 90))
        print('Ваш случайный номерной знак - нового типа: ', mark)

def main():
    generate()
main()