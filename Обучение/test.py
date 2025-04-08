from tkinter import *
import time


root = Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = "white"


canvas = Canvas(root, width=800,height=600,bg="white")


def draw():
    canvas.move(hero,1,2)


hero = canvas.create_oval(80,80,120,120,fill="red")



while True:
    root.update()
    root.update_idletasks()
    draw()
    time.sleep(0.01)
