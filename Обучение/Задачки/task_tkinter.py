from tkinter import *

root = Tk()
root.title("Test")
root.geometry("800x600")

canvas = Canvas(root, width=700, height=500, bg="blue")
canvas.pack()

# Создаем основной прямоугольник и его тень
figure = canvas.create_rectangle(15, 15, 75, 75, fill="red")
shadow_f = canvas.create_rectangle(25, 25, 85, 85, fill="black")

# Перемещаем тень под прямоугольник
canvas.tag_lower(shadow_f, figure)

# Функции движения, которые перемещают и прямоугольник, и тень
def move_up(event):
    canvas.move(figure, 0, -10)
    canvas.move(shadow_f, 0, -10)

def move_left(event):
    canvas.move(figure, -10, 0)
    canvas.move(shadow_f, -10, 0)

def move_down(event):
    canvas.move(figure, 0, 10)
    canvas.move(shadow_f, 0, 10)

def move_right(event):
    canvas.move(figure, 10, 0)
    canvas.move(shadow_f, 10, 0)

# Привязываем функции движения к клавишам W, A, S, D
root.bind('w', move_up)
root.bind('a', move_left)
root.bind('s', move_down)
root.bind('d', move_right)

root.mainloop()
