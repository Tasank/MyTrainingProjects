"""
Упражнение 48. Знаки зодиака.
Напишите программу, запрашивающую у пользователя дату его рождения и выводящую на экран соответствующий знак зодиака.
"""
# .strip() чтобы удалить пробелы
month = input('Введите месяц дня рождения: ').strip().lower()
day = int(input('Введите день дня рождения: '))

# Блок проверки условий
if (month == 'декабрь' and 22 <= day <= 31) or (month == 'январь' and 1 <= day <= 19):
    print('Знак зодиака - Козерог')

elif (month == 'январь' and 20 <= day <= 31) or (month == 'февраль' and 1 <= day <= 18):
    print('Знак зодиака - Водолей')

elif (month == 'февраль' and 19 <= day <= 29) or (month == 'март' and 1 <= day <= 20):
    print('Знак зодиака - Рыбы')

elif (month == 'март' and 21 <= day <= 31) or (month == 'апрель' and 1 <= day <= 19):
    print('Знак зодиака - Овен')

elif (month == 'апрель' and 20 <= day <= 30) or (month == 'май' and 1 <= day <= 20):
    print('Знак зодиака - Телец')

elif (month == 'май' and 21 <= day <= 31) or (month == 'июнь' and 1 <= day <= 20):
    print('Знак зодиака - Близнецы')

elif (month == 'июнь' and 21 <= day <= 30) or (month == 'июль' and 1 <= day <= 22):
    print('Знак зодиака - Рак')

elif (month == 'июль' and 23 <= day <= 31) or (month == 'август' and 1 <= day <= 22):
    print('Знак зодиака - Лев')

elif (month == 'август' and 23 <= day <= 31) or (month == 'сентябрь' and 1 <= day <= 22):
    print('Знак зодиака - Дева')

elif (month == 'сентябрь' and 23 <= day <= 30) or (month == 'октябрь' and 1 <= day <= 22):
    print('Знак зодиака - Весы')

elif (month == 'октябрь' and 23 <= day <= 31) or (month == 'ноябрь' and 1 <= day <= 21):
    print('Знак зодиака - Скорпион')

elif (month == 'ноябрь' and 22 <= day <= 30) or (month == 'декабрь' and 1 <= day <= 21):
    print('Знак зодиака - Стрелец')

else:
    print('Ошибка ввода')