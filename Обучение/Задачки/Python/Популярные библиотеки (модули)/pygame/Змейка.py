import pygame
import pygame_menu.themes
import Меню

pygame.init()

# Константы
WIDTH = 800
HEIGHT = 600
FPS = 5

# Переменные
state = 'menu'
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Змейка')

