"""
Делаем анимацию пулемёта с помощью tkinter
"""

import time
from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = 'white'

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Создаём 2 объекта которые нарисуют простенькое дуло
canvas.create_rectangle(0, 180, 40, 200, fill="black")
canvas.create_rectangle(0, 250, 40, 270, fill="black")

# Создаём пулю (шарик красный)
hero = canvas.create_oval(5, 205, 45, 245, fill="red")

# Переменные скорости
h_x = 5
h_y = 0

def draw():
    global h_x, h_y, e_x, e_y
    x, y, x1, y1 = canvas.coords(hero)

    # Проверки для красного шарика
    if x <= 0:  # если мяч коснулся левой стенки
        h_x = -h_x  # меняем его Х-скорость на противоположную
    if x1 >= 800:  # если мяч коснулся правой стенки
        h_x = -h_x  # меняем его Х-скорость на противоположную

    if y <= 0:
        h_y = -h_y
    if y1 >= 600:
        h_y = -h_y

    canvas.move(hero, h_x, h_y)

while True:
    root.update()
    root.update_idletasks()
    draw() # Зацикливаем движение
    time.sleep(0.01)