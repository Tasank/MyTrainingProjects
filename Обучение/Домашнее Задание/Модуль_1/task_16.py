import random
import time
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = "white"

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

canvas.create_rectangle(0, 180, 40, 200, fill="black")
canvas.create_rectangle(0, 250, 40, 270, fill="black")

bullets = []
bullet_color = "red"

def shot():
    hero = canvas.create_oval(5, 205, 45, 245, fill=bullet_color)
    b = (hero, 10, random.random())
    bullets.append(b)
    root.after(50, shot)

# Изменяем цвет пули на нажатие клавиши V
def ask_color(event):
   global bullet_color
   color_code = askcolor(title="Выбери цвет")
   color = color_code[1]
   bullet_color = color

canvas.bind_all("<v>", ask_color)

def draw():

    for bull in bullets:
        bullet = bull[0]
        h_x = bull[1]
        h_y = bull[2]
        canvas.move(bullet, h_x, h_y)
        x, y, x1, y1 = canvas.coords(bullet)
        if x1 >= 800:
            canvas.delete(bullet)
            bullets.remove(bull)





shot()
while True:
   root.update()
   root.update_idletasks()
   draw()
   time.sleep(0.01)


