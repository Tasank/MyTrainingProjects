import turtle

# Активация черепашки
t = turtle.Pen()

# Установка размера черепашки
t.shape("turtle")


# Передвижение черепашки
t.backward(200)

# Изменение размера линии
t.pensize(5)

# Изменить цвет линии
t.color("red")

# Поворот черепашки на указанное кол-во градусов
t.left(90)
t.forward(100)

# Заливка
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.fillcolor("violet")
t.end_fill()

turtle.mainloop()

