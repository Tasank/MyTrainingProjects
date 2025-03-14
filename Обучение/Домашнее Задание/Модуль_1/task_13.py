import turtle

t = turtle.Pen()
screen = turtle.Screen()

screen.setup(1000, 600)
screen.title('Ракушка')
screen.bgcolor('black')


t.pencolor('white')
t.speed(0)
# Цикл который рисует ракушку
for x in range(100):
    for i in range(5):
        t.left(144)
    t.circle(x / 2 + 10)
    t.left(9)
    t.forward(x / 4)


turtle.mainloop()
