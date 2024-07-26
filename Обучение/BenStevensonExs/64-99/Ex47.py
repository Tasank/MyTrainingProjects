"""
Упражнение 47. Определение времени года.
Разработайте программу, запрашивающую у пользователя день и месяц – сначала месяц в текстовом варианте, затем номер дня.
На выходе программа должна выдать название сезона, которому принадлежит выбранная дата.
"""

autumn_period = ['сентябрь', 'октябрь', 'ноябрь']
winter_period = ['декабрь', 'январь', 'февраль']
summer_period = ['июнь', 'июль', 'август']
spring_period = ['май', 'март', 'апрель']

month_input = input('Введите название месяца: ').lower()
day_input = int(input('Введите день: '))

if 1 > day_input or day_input > 31:
    print('Ошибка ввода (день).')
    quit()
if month_input == 'сентябрь' and 22 > day_input > 0:
    print('Летний сезон.')

elif month_input == 'декабрь' and 21 > day_input > 0:
    print('Осенний сезон.')
elif month_input == 'июнь' and 21 > day_input > 0:
    print('Весенний сезон.')
elif month_input == 'март' and 20 > day_input > 0:
    print('Зимний сезон.')

elif month_input in autumn_period:
    print('Осенний сезон.')
elif month_input in winter_period:
    print('Зимний сезон.')
elif month_input in summer_period:
    print('Летний сезон.')
elif month_input in spring_period:
    print('Весенний сезон.')

else:
    print('Ошибка ввода (месяц).')