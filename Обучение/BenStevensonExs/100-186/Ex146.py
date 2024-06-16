"""
Упражнение 146. Карточка лото.
Напишите функцию, которая будет создавать случайную карточку лото и сохранять ее в словаре.
Ключами словаря будут буквы B, I, N, G и O, а значениями – списки из пяти чисел, располагающихся в колонке под
каждой буквой. Создайте еще одну функцию для отображения созданной карточки лото на экране со столбцами с заголовками.
В основной программе создайте карту лото случайным образом и выведите ее на экран.
Ваша программа должна запускаться только в том случае, если она не импортирована в виде модуля в другой файл.
"""
from random import randint
def generate_random_card():
    """ Функция, которая будет создавать случайную карточку лото и сохранять ее в словаре"""
    BINGO_DICT = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    # count = 0
    # while count != 5:
    #     count += 1
    #     number_1 = randint(1, 15)
    #     BINGO_DICT['B'].append(number_1)
    #
    #     number_2 = randint(16, 30)
    #     BINGO_DICT['I'].append(number_2)
    #
    #     number_3 = randint(31, 45)
    #     BINGO_DICT['N'].append(number_3)
    #
    #     number_4 = randint(46, 60)
    #     BINGO_DICT['G'].append(number_4)
    #
    #     number_5 = randint(61, 75)
    #     BINGO_DICT['O'].append(number_5)

    ranges = {'B': (1, 15), 'I': (16, 30), 'N': (31, 45), 'G': (46, 60), 'O': (61, 75)}

    for letter in "BINGO":
        BINGO_DICT[letter] = [randint(ranges[letter][0], ranges[letter][1]) for _ in range(5)]

    return BINGO_DICT
def display_card(dict_card):
    """Функция для отображения созданной карточки лото на экране со столбцами с заголовками"""
    print(" B |  I |  N |  G |  O ")
    print("---|----|----|----|----")
    for i in range(5):
        print(f"{dict_card['B'][i]:2} | "
              f"{dict_card['I'][i]:2} | "
              f"{dict_card['N'][i]:2} | "
              f"{dict_card['G'][i]:2} | "
              f"{dict_card['O'][i]:2}")

def main():
    card = generate_random_card()
    display_card(card)

if __name__ == '__main__':
    main()