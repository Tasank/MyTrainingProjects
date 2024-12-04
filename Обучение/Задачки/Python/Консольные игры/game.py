print('Игра крестики-нолики')
print("_____________________")
print("       Правила       ")
print("Первые ходят крестики")
print("На ввод принимается только допустимые диапазон от 0 да 2")
print("Нельзя ходить на уже занятое поле!")

#Создадим игровое поле, где будут храниться память

field = [[" "] * 3 for i in range(3)]
count = 0

#Функция для отображения игрового поля
def display():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()
#Функция для проверки является ли ход победным
def check_win(player):
    # Все возможные комбинации для победы
    win_combination = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for combination in win_combination:
        symbols = []
        for c in combination:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Нолик!")
            return True
    return False

#Функция для хода Игрока
def move():
    while True:
        try:
            cords = input("         Ваш ход: ").split()
            row, col = cords
            row, col = int(row), int(col)
            if field[row][col] != " ":
                print(" Клетка занята! ")
                continue
            return row, col

        except ValueError:
            print('Некорректный ввод введите числа от (0 до 2) через пробел')

#Основная функция игры
def play_game():
    current_player = 'X'
    while True:
        global count
        count += 1
        display()

        if count % 2 == 1:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")

        row, col = move()

        if count % 2 == 1:
            field[row][col] = "X"
        else:
            field[row][col] = "0"


        if check_win(current_player):
            break

        if count == 9:
            print(" Ничья!")
            break

play_game()