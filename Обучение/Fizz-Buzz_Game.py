"""
 Упражнение 72. Игра Fizz-Buzz.
 Разработайте программу, реализующую алгоритм игры Fizz-Buzz применительно к первым 100 числам.
 Каждый следующий ответ должен отображаться на новой строке.
 Первый игрок говорит «Один» и передает ход тому, кто слева.
 Каждый следующий игрок должен мысленно прибавить к предыдущему числу единицу и произнести либо его,
 либо одно из ключевых слов: Fizz, если число без остатка делится на три, или Buzz, если на пять.
 Если соблюдаются оба этих условия, он произносит Fizz-Buzz
"""


print('____________________________________________________________________')
print('|                       Игра Fizz-Buzz                             |')
print('|Ваша задача угадать Fizz-Buzz. Игра продолжается до первой ошибки!|')
print('|    Победа достигается если вы указали правильное все 100 чисел!  |')
print('|__________________________________________________________________|')
print('|Введите:                                                          |')
print('|1) Fizz, если число без остатка делится на три                    |')
print('|2) Buzz, если число без остатка делится на пять                   |')
print('|3) Fizz-Buzz, если соблюдаются оба этих условия                   |')
print('|4) Нажмите Enter, если число не подходит ни к одному условию      |')
print('|__________________________________________________________________|')
print('|                        ИГРА НАЧАЛАСЬ!                            |')

count = 1
to_lose = False
to_win = False

while count != 100:
    # Вывод числа (разные пробелы, чтобы игровая панель была ровная)
    if count < 10:
        print('|Текущее число: %d                                                  |' % count)
    elif 100 > count >= 10:
        print('|Текущее число: %d                                                 |' % count)
    elif count == 100:
        print('|Текущее число: %d                                                |' % count)

    ask = input('|Определите число (Fizz/Buzz/Fizz Buzz/ Enter)                     | --> ')

    # Проверяем условие, если оно верно то игрок проиграл
    if ask != 'Fizz' and count % 3 == 0 and count % 5 != 0:
        to_lose = True
    elif ask != 'Buzz' and count % 5 == 0 and count % 3 != 0:
        to_lose = True
    elif ask != 'Fizz Buzz' and count % 3 == 0 and count % 5 == 0:
        to_lose = True

    # Проверяем условия на правильный ответ.
    # Можно было закончить на условиях "проигрыша", а в блок else вывести на экран "Верный ход"
    # Но тогда, чтобы не написал пользователь будет являться правильным ходом, будь то цифра или ещё что-нибудь
    elif ask == 'Fizz' and count % 3 == 0:
        to_win = True
    elif ask == 'Buzz' and count % 5 == 0:
        to_win = True
    elif ask == 'Fizz Buzz' and count % 3 == 0 and count % 5 == 0:
        to_win = True
    elif ask == '':
        pass
    else:
        print('|Я для тебя шутка какая-то? ТЫ ПРОИГРАЛ!                           |')
        break

    # Вывод правильного хода
    if to_win is True:
        print('|Вы молодец правильный ответ!                                      |')
        to_win = False

    # Вывод пройгрыша
    if to_lose is True:
        print('|Не правильный ответ! Вы проиграли!                                |')
        print('____________________________________________________________________')
        break

    count += 1

    if count == 100:
        print('Вы победили. УРА!')
    # Корректировка игровой панели
    print('|__________________________________________________________________|')
    if ask == '':
        print('|                       ⌛️Следующий ход⌛️                           |')