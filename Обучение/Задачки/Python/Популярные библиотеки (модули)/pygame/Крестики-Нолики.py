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
                pygame.draw.line(screen, 'black', (j * 200 + 5, i * 200 +5), (j * 200 + 195, i * 200 + 195), 5)
                pygame.draw.line(screen, 'black', (j * 200 + 5, i * 200 + 195), (j * 200 + 195, i * 200 + 5), 5)
            elif field[i][j] == 'o':
                pygame.draw.circle(screen, 'black', (j * 200 + 100, i * 200 + 100), 90, 5)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-Нолики')

# Создание меню
main_menu = Меню.Menu(screen, theme=Меню.themes.THEME_GREEN)
main_menu.add.selector('Выберите сторону: ', [('Крестики', True), ('Нолики', False)], onchange=set_side)

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

    screen.fill('gray')
    draw_grid()
    draw_symbols()
    main_menu.flip(events)

    pygame.display.flip()

pygame.quit()