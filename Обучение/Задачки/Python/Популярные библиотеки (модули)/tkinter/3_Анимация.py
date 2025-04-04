import time
from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = 'white'

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Создаём шарики которые будем анимировать
hero = canvas.create_oval(80, 80, 120, 120, fill="red")
evil = canvas.create_oval(130, 80, 170, 120, fill="blue")

# Переменные скорости
h_x = 4
h_y = 5

e_x = 5
e_y = 5

def draw():
    global h_x, h_y, e_x, e_y
    x, y, x1, y1 = canvas.coords(hero)
    ex, ey, ex1, ey1 = canvas.coords(evil)

    # Проверки для красного шарика
    if x <= 0:  # если мяч коснулся левой стенки
        h_x = -h_x  # меняем его Х-скорость на противоположную
    if x1 >= 800:  # если мяч коснулся правой стенки
        h_x = -h_x  # меняем его Х-скорость на противоположную

    if y <= 0:
        h_y = -h_y
    if y1 >= 600:
        h_y = -h_y

    # Проверки для синего шарика
    if ex <= 0:
        e_x = -e_x
    if ex1 >= 800:
        e_x = -e_x

    if ey <= 0:
        e_y = -e_y
    if ey1 >= 600:
        e_y = -e_y

    canvas.move(hero, h_x, h_y)
    canvas.move(evil, e_x, e_y)

while True:
    root.update()
    root.update_idletasks()
    draw() # Зацикливаем движение
    time.sleep(0.01)
