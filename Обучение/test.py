import turtle
t = turtle. Pen()
t.color("yellow")
t.begin_fill()

for x in range(80):
    t.forward(5)
    t.left(5)
t.end_fill()

turtle.mainloop()