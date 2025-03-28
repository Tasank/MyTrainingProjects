from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.title("Холст")
root.geometry("600x400")
root['bg'] = 'gray75'

canvas = Canvas(root, width=540, height=400, bg="white")
canvas.grid(row=0, column=0, rowspan=7)

# Создаём объект текста, который будет отвечать за размер и цвет ручки
brush = 10
color = 'red'

size_pen = Label(root, text=brush, fg=color, font='None 32')
size_pen.grid(row=6, column=1)


def choose(input):
    global state, brush

    if input == "plus" and brush < 98:
        brush += 2
        size_pen.configure(text=brush)
        return

    elif input == "minus" and brush > 0:
        brush -= 2
        size_pen.configure(text=brush)
        return

    state = input


# Создание кнопок, чтобы добавить кнопку в функцию choose используем lambda функцию
square_btn = Button(root, text="🟥", font=(None, 20), command=lambda: choose('square'))
circle_btn = Button(root, text="🔴", font=(None, 20), command=lambda: choose("circle"))
line1_btn = Button(root, text=" ↘ ", font=(None, 20), command=lambda: choose("line1"))
line2_btn = Button(root, text=" ↙ ", font=(None, 20), command=lambda: choose("line2"))
plus_btn = Button(root, text="➕", font=(None, 20), command=lambda: choose("plus"))
minus_btn = Button(root, text="➖", font=(None, 20), command=lambda: choose("minus"))

# Размещение кнопок
square_btn.grid(row=0, column=1)
circle_btn.grid(row=1, column=1)
line1_btn.grid(row=2, column=1)
line2_btn.grid(row=3, column=1)
plus_btn.grid(row=4, column=1)
minus_btn.grid(row=5, column=1)


# Функция, которая будет отвечать за рисование
def paint(event):
    # Если нажатие произошло не на холсте, то рисование не начинается.
    if event.widget.__class__ is not Canvas:
        return

    if state == 'circle':
        canvas.create_oval(event.x - brush,  # Координата x1
                           event.y - brush,  # Координата y1
                           event.x + brush,  # Координата x2
                           event.y + brush,  # Координата y2
                           fill=color,  # Цвет заливки
                           outline=color)  # Цвет обводки
    elif state == "square":
        canvas.create_rectangle(event.x - brush,
                                event.y - brush,
                                event.x + brush,
                                event.y + brush,
                                fill=color,
                                outline=color)
    elif state == "line1":
        canvas.create_line(event.x - brush,
                           event.y - brush,
                           event.x + brush,
                           event.y + brush,
                           fill=color)
    elif state == "line2":
        canvas.create_line(event.x + brush,
                           event.y - brush,
                           event.x - brush,
                           event.y + brush,
                           fill=color)
    print(event.__dict__)


# Бинд рисование на клик
root.bind_all('<1>', paint)
root.bind_all("<B1-Motion>", paint)


# Функция ластика
def erase(event):
    canvas.create_oval(event.x - brush * 2,
                       event.y - brush * 2,
                       event.x + brush * 2,
                       event.y + brush * 2,
                       fill="white",
                       outline="white")


root.bind_all("<3>", erase)
root.bind_all("<B3-Motion>", erase)

root.mainloop()
