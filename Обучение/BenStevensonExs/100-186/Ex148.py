"""
Упражнение 148. Играем в лото.
В данном упражнении мы напишем программу, выполняющую симуляцию игры в лото с одной картой.
Начните с генерирования списка из всех возможных номеров для выпадения (от B1 до O75). После этого перемешайте номера в
хаотичном порядке, воспользовавшись функцией shuffle из модуля random. Вытаскивайте по одному номеру из списка и
зачеркивайте номера, пока карточка не окажется выигравшей. Проведите 1000 симуляций и выведите на экран минимальное,
максимальное и среднее количество извлечений номеров, требующееся для выигрыша.
При решении этой задачи вы можете воспользоваться функциями из упражнений 146 и 147.
"""
from random import shuffle

from Ex147 import *
from Ex146 import *

def simulate_bingo():
    all_numbers = all_numbers = [f"{letter}{num}" # Формирование номеров
                                 for letter in 'BINGO'
                                 for num in range(1 + 'BINGO'.index(letter)*15, 16 + 'BINGO'.index(letter)*15)]
    shuffle(all_numbers)

    # Генерация карты
    card = generate_random_card()

    # Инициализация счетчика вытаскиваний
    drawn_numbers = 0

    # Вытаскивания номеров и зачёркивание на карте
    for number in all_numbers:
        drawn_numbers += 1
        # Разделяем Букву и номер
        letter, num = number[0], int(number[1:])
        if num in card[letter]:
            # Зачёркиваем если номер найден (заменяем на 0)
            card[letter][card[letter].index(num)] = 0
        # Если карта выигранная возвращаем drawn_numbers
        if is_winning_card(card):
            return drawn_numbers

def main():
    simulation = 1000
    results = [simulate_bingo() for i in range(simulation)]

    print(f"Минимальное количество вытаскиваний: {min(results)}")
    print(f"Максимальное количество вытаскиваний: {max(results)}")
    print(f"Среднее количество вытаскиваний: {sum(results) / simulation: .1f}")

if __name__ == '__main__':
    main()
