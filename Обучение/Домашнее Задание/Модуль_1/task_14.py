from tkinter import *
from random import *

# Настройка окна
root = Tk()
root.title('Игра: Угадай')
root.geometry('800x400')
root['bg'] = 'teal'


# Создание 4 кнопок с рандомными цветами
colors = ['red', 'green', 'blue', 'yellow']
buttons = [Button(root, bg=color) for color in colors]





root.mainloop()