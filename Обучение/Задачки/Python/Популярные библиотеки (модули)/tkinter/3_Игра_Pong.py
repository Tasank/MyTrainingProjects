from tkinter import *

root = Tk()
root.geometry('800x600')
root.title('Ping-Pong')

canvas = Canvas(root, width=800, height=600, bg='black')
canvas.pack()


class Player:
    def __init__(self):
        self.id = None
        self.y = 0
        self.speed = 3

    def draw(self):
        if self.id is not None:
            canvas.move(self.id, 0, self.y)
            _, y, _, y1 = canvas.coords(self.id)
            if y <= 0 or y1 >= 600:
                self.y = 0


class Player1(Player):
    def __init__(self):
        super().__init__()
        self.id = canvas.create_rectangle(30, 10, 20, 90, fill='white')

    def move(self, event):
        if event.keysym == 'w':
            self.y = -self.speed
        if event.keysym == 's':
            self.y = self.speed

    def stop(self, event):
        if event.keysym in ("w", "s"):
            self.y = 0


class Player2(Player):
    def __init__(self):
        super().__init__()
        self.id = canvas.create_rectangle(760, 10, 770, 90, fill="white")

    def move(self, event):
        if event.keysym == 'Up':
            self.y = -self.speed
        if event.keysym == 'Down':
            self.y = self.speed

    def stop(self, event):
        if event.keysym in ("Up", "Down"):
            self.y = 0


class Ball:
    def __init__(self):
        self.id = canvas.create_oval(40, 20, 70, 50, fill="white")
        self.x = 3
        self.y = 3

    def draw(self):
        global score
        canvas.move(self.id, self.x, self.y)
        bx, by, bx1, by1 = canvas.coords(self.id)

        if by <= 0 or by1 >= 600:
            self.y = -self.y

        x1, y1, x11, y11 = canvas.coords(player1.id)
        x2, y2, x22, y22 = canvas.coords(player2.id)

        # Отскок от первого игрока и начисление очка
        if by <= y11 and by1 >= y1 and bx <= x11:
            self.x = abs(self.x)
            player1.speed += 0.25
            self.x += 0.25
            score += 1
            canvas.itemconfig(score_gui, text=f"Счёт: {score}")

        # Отскок от второго игрока и начисление очка
        if by <= y22 and by1 >= y2 and bx1 >= x2:
            self.x = -abs(self.x)
            player2.speed += 0.25
            self.x -= 0.25
            score += 1
            canvas.itemconfig(score_gui, text=f"Счёт: {score}")

        # Проверка на конец игры (мяч достиг левой или правой стенки)
        if bx <= 0 or bx1 >= 800:
            return True
        return False


score = 0

player1 = Player1()
player2 = Player2()
ball = Ball()

root.bind_all('<KeyPress-w>', player1.move)
root.bind_all('<KeyPress-s>', player1.move)
root.bind_all('<KeyRelease-w>', player1.stop)
root.bind_all('<KeyRelease-s>', player1.stop)

root.bind_all('<KeyPress-Up>', player2.move)
root.bind_all('<KeyPress-Down>', player2.move)
root.bind_all('<KeyRelease-Up>', player2.stop)
root.bind_all('<KeyRelease-Down>', player2.stop)

score_gui = canvas.create_text(390, 20, text="Счёт: 0", fill="white", font=("Consolas", 20))
record_gui = canvas.create_text(390, 40, text="Рекорд: 0", fill="white", font=("Consolas", 20))

# Проверка на наличие файла
try:
    with open("score.ini", "r") as record_file:
        data = record_file.readline()
        record = int(data) if data else 0
except FileNotFoundError:
    record = 0
    with open("score.ini", "w") as record_file:
        record_file.write(str(record))

canvas.itemconfig(record_gui, text=f"Рекорд: {record}")


def game_loop():
    global score, record
    player1.draw()
    player2.draw()

    if ball.draw():  # Если мяч коснулся левой или правой стенки
        if score > record:
            record = score
            with open("score.ini", "w") as record_file:
                record_file.write(str(record))
            canvas.itemconfig(record_gui, text=f"Рекорд: {record}")
        print("Игре Конец") # Это выводится в консоль
        print(f"Ваш счёт: {score}, Рекорд: {record}")
        return  # Завершить игру

    root.after(16, game_loop)


game_loop()
root.mainloop()
