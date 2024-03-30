"""
Упражнение 108. Переводим меры.
Напишите функцию, выражающую заданный объем ингредиентов с использованием минимально возможных замеров.
Функция должна принимать в качестве параметра количество единиц измерения, а также их тип (стакан,
столовая или чайная ложка). На выходе мы должны получить строку, представляющую указанное количество вещества,
с задействованием минимального количества действий и предметов. Например, если на вход функции вы подали объем,
равный 59 чайным ложкам, возвращенная строка должна быть такой: «1 cup, 3 tablespoons, 2 teaspoons».
"""

def conversion(unit, type_v):
    cup = 0
    tablespoons = 0
    teaspoons = 0

    # Основная логика функции, присваивание переменным значения
    if type_v == 'cup':
        cup = unit

    if type_v == 'teaspoons':
        teaspoons = unit
        cup = teaspoons // 48
        teaspoons = teaspoons % 48
        tablespoons = teaspoons // 3
        teaspoons = teaspoons % 3

    if type_v == 'tablespoons':
        tablespoons = unit
        cup = tablespoons // 16
        tablespoons = tablespoons % 16
        teaspoons = 0
    else:
        return 'ОШИБКА'

    # Добавление s если есть множество
    if cup > 1:
        cup = str(cup) + ' cups'
    else:
        cup = str(cup) + ' cup'

    if tablespoons > 1:
        tablespoons = str(tablespoons) + ' tablespoons'
    else:
        tablespoons = str(tablespoons) + ' tablespoons'

    if teaspoons > 1:
        teaspoons = str(teaspoons) + ' teaspoons'
    else:
        teaspoons = str(teaspoons) + ' teaspoon'

    return cup, tablespoons, teaspoons

def main():
    unit = int(input('Введите объём: '))
    type_v = input('Введите тип (cup, tablespoons, teaspoons): ')
    print('Минимально удобный рецепт: ', *conversion(unit, type_v))

main()