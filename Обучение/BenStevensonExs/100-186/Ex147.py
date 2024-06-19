"""
Упражнение 147. Проверка карточки.
Карточка для игры в лото считается выигравшей, если в ней на одной линии расположились пять выпавших номеров.
Обычно игроки зачеркивают номера на своих карточках. В данном упражнении мы будем обнулять в словаре выпавшие номера.
Напишите функцию, принимающую на вход карточку в качестве параметра.
Если карточка содержит последовательность из пяти нулей (по вертикали, горизонтали или диагонали),
функция должна возвращать True, в противном случае – False.
В основной программе вы должны продемонстрировать на примере работу функции, создав и отобразив несколько карточек с
указанием того, какие из них выиграли. В вашем примере должно быть как минимум по одной карточке с
выигрышем по вертикали, горизонтали и диагонали, а также карточки, на которые выигрыш не выпал.
При решении этой задачи воспользуйтесь функциями из упражнения 146.
"""
from Ex146 import *
def is_winning_card(dict_card):
    """Проверка вертикальных линий"""
    # Если все числа в списке, соответствующему текущей букве, равны 0
    for letter in 'BINGO':
        if all(num == 0 for num in dict_card[letter]):
            return True

    """Проверка горизонтальных линий"""
    for i in range(5):
        if all(dict_card[letter][i] == 0 for letter in 'BINGO'): # dict_card[letter][i] обращаемся к значению в словаре
            return True

    """Проверка диагональных линий"""
    # Проверка слева направо, сверху вниз
    if all(dict_card['BINGO'[i]][i] == 0 for i in range(5)):
        return True
    # Проверка справа налево, сверху вниз
    if all(dict_card['BINGO'[i]][4 - i] for i in range(5)):
        return True

def demonstrate_winning_card():
    # Пример горизонтальной выигрышной карточки
    horizontal_win_card = generate_random_card()
    horizontal_win_card['B'] = [0, 0, 0, 0, 0]

    # Пример вертикальной выигрышной карточки
    vertical_win_card = generate_random_card()
    for letter in "BINGO":
        vertical_win_card[letter][0] = 0

    # Пример диагональной выигрышной карточки
    diagonal_win_card = generate_random_card()
    for i in range(5):
        diagonal_win_card["BINGO"[i]][i] = 0

    # Пример карточки без выигрыша
    no_win_card = generate_random_card()

    cards = [horizontal_win_card, vertical_win_card, diagonal_win_card, no_win_card]
    results = ["Горизонтальный выйгрыш", "Вертикальный выйгрыш", "Диагональный выйгрыш", "Пройгрыш"]

    # zip принимает несколько аргументов и объединяет элементы этих объектов в кортежи
    for card, result in zip(cards, results):
        print(f"Тип карты: {result}")
        display_card(card)
        print(f"Победа: {is_winning_card(card)}")
        print()

def main():
    demonstrate_winning_card()

if __name__ == '__main__':
    main()

