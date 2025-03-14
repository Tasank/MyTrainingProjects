import turtle


# Создаем черепашек
red = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()

# Меняем им цвет
red.color("red")
blue.color("dark blue")
yellow.color("yellow")
green.color("green")

# Меняем им скорость
red.speed(0)
blue.speed(0)
yellow.speed(0)
green.speed(0)

# Синяя черепашка рисует спираль
blue.penup()
blue.goto(-200, -150)
blue.pendown()

for i in range(60):
    blue.color(i / 60, 0, 1 - i / 360)
    blue.forward(i * 2)
    blue.right(59)
    for _ in range(2):
        blue.forward(i * 2)
        blue.right(59)

# зелёная черепашка рисует квадрат
green.penup()
green.goto(-200, 150)
green.pendown()

for _ in range(4):
    green.forward(100)
    green.right(90)

# Желтая черепашка рисует солнце
yellow.penup()
yellow.goto(200, 150)
yellow.pendown()
yellow.pensize(4)

yellow.begin_fill()
for _ in range(22):
    yellow.right(45)
    yellow.forward(50)
    yellow.left(145)
    yellow.forward(50)
yellow.end_fill()




# Красная черепашка рисует круговую спираль
red.penup()
red.goto(200, -150)
red.pendown()

for _ in range(36):
    for _ in range(36):
        red.forward(10)
        red.right(10)
    red.right(10)




turtle.mainloop()
