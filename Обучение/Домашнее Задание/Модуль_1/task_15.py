import tkinter as tk
import random

# Создаем главное окно
root = tk.Tk()
root.title("Угадай кнопку")
root.geometry("800x600")
root['bg'] = 'light blue'

text = tk.Label(root, text="Попробуй угадать загаданный цвет", bg='light blue', fg='black', font=('Arial', 20))
text.pack(side='top', pady=20)

# Функция для обработки нажатий на кнопки
def check_button(selected_button):
    if selected_button == correct_button:
        label.config(text="Ты угадал!")
    else:
        for btn in buttons:
            if btn != correct_button:
                btn.place_forget() # метод place_forget() удаляет виджет из интерфейса
        label.config(text="Ты не угадал >:(")

# Создаем метку для отображения результата
label = tk.Label(root, bg='light blue', fg='black', font=('Arial', 20))
label.pack(side='bottom', pady=20)

# Создаем кнопки
buttons = [
    tk.Button(root, bg='red', width=20, height=10, text='Нажми на меня', command=lambda: check_button(btn_1)),
    tk.Button(root, bg='green', width=20, height=10, text='Нажми на меня', command=lambda: check_button(btn_2)),
    tk.Button(root, bg='teal', width=20, height=10, text='Нажми на меня', command=lambda: check_button(btn_3)),
    tk.Button(root, bg='blue', width=20, height=10, text='Нажми на меня', command=lambda: check_button(btn_4)),
]

# Назначаем случайную правильную кнопку
correct_button = random.choice(buttons)

# Размещаем кнопки в центре (в виде таблицы)
buttons[0].place(x=100, y=100)
buttons[1].place(x=100, y=300)
buttons[2].place(x=500, y=100)
buttons[3].place(x=500, y=300)

btn_1, btn_2, btn_3, btn_4 = buttons

root.mainloop()
