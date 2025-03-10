import turtle

pen = turtle.Pen()
pen.shape("turtle")
pen.pensize(7)


# Рисуем солнце
pen.color('yellow')

pen.begin_fill()
for i in range(72):
    pen.left(5)
    pen.forward(5)

pen.end_fill()


# Делаем так чтобы часть солнца было закрыто морем
pen.left(90)
pen.forward(30)
pen.right(90)

# Рисуем прямоугольник (море)
pen.color("blue")
pen.begin_fill()
pen.forward(300)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(600)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(300)
pen.end_fill()



turtle.mainloop()