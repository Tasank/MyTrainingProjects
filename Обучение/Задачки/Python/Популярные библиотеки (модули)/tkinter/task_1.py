from tkinter import *

# Создание скелета интерфейса
root = Tk()

# Настройка интерфейса
root.title('Мой первый графический интерфейс')
root.geometry('400x300')
root['bg'] = 'black'

# Создание виджета
text = Label(root, text='Первый виджет', font='Arial 16', bg='black', fg='white')
# Команда pack() размещает виджет в интерфейсе
text.pack()

text_2 = Label(root, text='𓁈𓂀𓋹𓆣𓁀𓀾', font='Arial 100', bg='black', fg='white')
text_2.pack()

# Создание функциональности
def delete_text():
    text.destroy()

# Создание кнопки
button = Button(root, text='Узнать тайну', font='Arial 16', bg='black', fg='white',
    command=delete_text)
button.pack()

root.mainloop()