from tkinter import *


root = Tk()
root.title("-")
root.geometry("800x600")
root['bg'] = 'light blue'

canvas = Canvas(root, width=800, height=600, bg='light blue')
# Забиндить удаление холста на кнопку BackSpace, А также забиндить подбор цвета на кнопку C
def clear_canvas(event):
    canvas.delete("all")
def ask_color(event):
    # ...
    pass
root.bind_all("<c>", ask_color)
root.bind_all("<BackSpace>", clear_canvas)
#....

root.mainloop()