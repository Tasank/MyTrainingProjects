"""
Напишите функцию, которая запрашивает у пользователя: массу арбуза(кг),
его первоначальную влажность(от 0.01 до 0.99) и значение этой влажности изменённого спустя время.
Результат функция должна выводить новую массу арбуза.
"""
def arbuz():
    weight = float(input('Введите вес арбуза: '))
    wetness = float(input('Введите влажность арбуза (от 0 до 1): '))
    new_wetness = float(input('Введите влажность арбуза через (n) дней (от 0 до 1): '))

    if not (0 <= wetness <= 1) or not (0 <= new_wetness <= 1):
        return "Некорректные значения влажности. Введите значения от 0 до 1."

    initial_humidity = wetness * weight
    dry = weight - initial_humidity

    new_humidity = 1.0 - new_wetness
    if new_humidity == 0:
        return "Ошибка: новая влажность равна 100%, невозможно рассчитать массу сухого вещества."

    result = dry / new_humidity
    return round(result, 2)

print(arbuz())
