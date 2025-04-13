from tkinter import *

root = Tk()
root.geometry('800x600')
root.title('Ping-Pong')

canvas = Canvas(root, width=800, height=600, bg='black')
canvas.pack()

class Ball:
   def __init__(self):
       self.id = canvas.create_oval(40, 20, 70, 50, fill="white")
       self.x = 3
       self.y = 3
