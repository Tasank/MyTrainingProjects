"""
Упражнение 60. На какой день недели выпадает 1 января?
Используйте эту формулу для написания программы, запрашивающей у пользователя год и выводящей на экран день недели,
на который в заданном году приходится 1 января. При этом на экран вы должны вывести не числовой эквивалент дня недели,
а его полное название.
"""
from math import floor

year = int(input('Введите год: '))

day_of_the_week = (year + floor((year - 1)/4) - floor((year - 1)/100) + floor((year - 1)/400)) % 7

if day_of_the_week == 0:
    day = 'воскресенье'
elif day_of_the_week == 1:
    day = 'понедельник'
elif day_of_the_week == 2:
    day = 'вторник'
elif day_of_the_week == 3:
    day = 'среда'
elif day_of_the_week == 4:
    day = 'четверг'
elif day_of_the_week == 5:
    day = 'пятница'
elif day_of_the_week == 6:
    day = 'суббота'

else:
    print('Ошибка ввода')
    quit()

print(f'1 января в {year} году будет {day}')
