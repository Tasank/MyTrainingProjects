import pygame

pygame.init()

WIDTH = 480
HEIGHT = 360

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Шаблон')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False



pygame.quit()