import random

import pygame

import Меню

pygame.init()

# Константы
WIDTH = 600
HEIGHT = 600
FPS = 60

# Переменные
posY = 20
posX = 20
speed = 15
player_side = 'x'
comp_side = 'o'
state = 'menu'

# Игровое поле
field = [['', '', ''] for _ in range(3)]

# Функция изменения стороны
def set_side(_, side):
    global player_side, comp_side
    if side:
        player_side = 'x'
        comp_side = 'o'
    else:
        player_side = 'o'
        comp_side = 'x'


# Функция отрисовки поля
def draw_grid():
    for c in range(1, 3):
        pygame.draw.line(screen, 'black', (c * 200, 0) , (c * 200, 600), 3)
    for r in range(1, 3):
        pygame.draw.line(screen, 'black', (0, r * 200), (600, r * 200), 3)

# Функция проверки состояния игры
def disable():
    global state
    main_menu.disable()
    state = 'game'

# Функция отрисовки символов на поле
def draw_symbols():
    # i - строка, j - столбец
    for i in range(3):
        for j in range(3):
            if field[i][j] == 'x':
                pygame.draw.line(screen, 'black', (j * 200 + 50, i * 200 + 50), (j * 200 + 150, i * 200 + 150), 5)
                pygame.draw.line(screen, 'black', (j * 200 + 50, i * 200 + 150), (j * 200 + 150, i * 200 + 50), 5)
            elif field[i][j] == 'o':
                pygame.draw.circle(screen, 'black', (j * 200 + 100, i * 200 + 100), 50, 5)


# Функция хода компьютера
def comp_move():
    while True:
        row, column = random.randint(0, 2), random.randint(0, 2)
        if field[row][column] != '':
            continue
        else:
            field[row][column] = comp_side
            break

# Функция победы
def check_win():
    win = []
    for side in 'xo':
        # Проверка горизонтальных линий
        for row in range(3):
            if field[row].count(side) == 3:
                win = [(0, row), (1, row), (2, row)]
                if side == player_side:
                    pygame.display.set_caption('Вы победили!')
                else:
                    pygame.display.set_caption('Вы проиграли!')
                return win

        # Проверка вертикальных линий
        for col in range(3):
            if field[0][col] == field[1][col] == field[2][col] == side:
                win = [(col, 0), (col, 1), (col, 2)]
                if side == player_side:
                    pygame.display.set_caption('Вы победили!')
                else:
                    pygame.display.set_caption('Вы проиграли!')
                return win

        # Проверка диагоналей
        if field[0][0] == field[1][1] == field[2][2] == side:
            win = [(0, 0), (1, 1), (2, 2)]
            if side == player_side:
                pygame.display.set_caption('Вы победили!')
            else:
                pygame.display.set_caption('Вы проиграли!')
            return win

        if field[0][2] == field[1][1] == field[2][0] == side:
            win = [(0, 2), (1, 1), (2, 0)]
            if side == player_side:
                pygame.display.set_caption('Вы победили!')
            else:
                pygame.display.set_caption('Вы проиграли!')
            return win

    return win


# Функция отрисовки выйгрышных линий
def draw_win(win):
    if win:
        for x, y in win:
            pygame.draw.rect(screen, 'green', (x * 200, y * 200, 200, 200), 5)

        pygame.time.delay(1000)


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-Нолики')

# Создание меню
main_menu = Меню.Menu(screen, theme=Меню.themes.THEME_GREEN)
main_menu.add.selector('Выберите сторону: ', [('Крестик', True), ('Нолик', False)], onchange=set_side)

main_menu.add.button('Играть', disable)
main_menu.add.button('Выход', pygame.quit)



clock = pygame.time.Clock()

run = True
while run:
    clock.tick(FPS)

    # Обработка событий
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Меняем состояние, чтобы в меню не отслеживалось нажатие мыши
                state = 'menu'
                main_menu.enable()
        elif event.type == pygame.MOUSEBUTTONDOWN and state == 'game':
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 200][pos[0] // 200] == '':
                field[pos[1] // 200][pos[0] // 200] = player_side
                comp_move()


    screen.fill('gray')
    win = check_win()
    draw_win(win)
    draw_grid()
    draw_symbols()
    main_menu.flip(events)

    pygame.display.flip()

pygame.quit()