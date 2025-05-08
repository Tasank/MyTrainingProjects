import pygame

pygame.init()

# Константы
WIDTH = 800
HEIGHT = 600
FPS = 60

# Переменные
posY = 20
posX = 20
speed = 15


screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание окна
pygame.display.set_caption('Шаблон') # Изменение заголовка


clock = pygame.time.Clock()


pygame.display.flip()

run = True
while run:
    clock.tick(FPS)
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posX -= speed
            elif event.key == pygame.K_RIGHT:
                posX += speed
            elif event.key == pygame.K_UP:
                posY -= speed
            elif event.key == pygame.K_DOWN:
                posY += speed

    # Цвет фона серый
    screen.fill('gray')

    # Рисуем фигуры
    pygame.draw.rect(screen, 'red', (posX, posY, 100, 100))
    pygame.draw.circle(screen, 'green', (300, 300), 50)
    pygame.draw.polygon(screen, 'white', [(400, 100), (500, 200), (600, 100)])

    pygame.display.flip()  # Обновление экрана, иначе цвет не установится

pygame.quit()