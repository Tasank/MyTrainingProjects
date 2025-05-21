from tkinter import *
from playsound3 import playsound

root = Tk()
root.geometry("800x600")
root.title("Pong")

canvas = Canvas(root, width=800, height=600, bg="black")
canvas.pack()

# Инициализация счета и рекорда
try:
    record_file = open("score.ini", "r+")
    data = record_file.readline()
    if data == "":
        record = 0
        record_file.write(f"{record}")
        record_file.close()
    else:
        record = int(data)
except:
    record = 0

score = 0

# Создание отображения счета на экране
score_gui = canvas.create_text(390, 20, text=f"Счет: {score}", fill="white", font=("Consolas", 20))
canvas.create_text(390, 40, text=f"Рекорд: {record}", fill="white", font=("Consolas", 20))

# Родительский класс игроков (ракеток)
class Player:
    def __init__(self):
        self.id = None
        self.y = None
        self.speed = None

    def draw(self):
        canvas.move(self.id, 0, self.y)
        _, y, _, y1 = canvas.coords(self.id)
        if y <= 0 or y1 >= 600:
            self.y = 0


class Player1(Player):
    def __init__(self):
        super().__init__()
        self.id = canvas.create_rectangle(30, 110, 40, 190, fill="white")
        self.y = 0
        self.speed = 3

    def move(self, event):
        if event.keysym == "w":
            self.y = -self.speed
        if event.keysym == "s":
            self.y = self.speed

    def stop(self, event):
        if event.keysym in "ws":
            self.y = 0


class Player2(Player):
    def __init__(self):
        super().__init__()
        self.id = canvas.create_rectangle(760, 210, 770, 290, fill="white")
        self.y = 0
        self.speed = 3

    def move(self, event):
        if event.keysym == "Up":
            self.y = -self.speed
        if event.keysym == "Down":
            self.y = self.speed

    def stop(self, event):
        if event.keysym in ("Up", "Down"):
            self.y = 0


class Ball:
    def __init__(self):
        self.id = canvas.create_oval(370, 290, 400, 320, fill="white")
        self.x_speed = 2
        self.y_speed = 2

    def draw(self):
        global score
        canvas.move(self.id, self.x_speed, self.y_speed)
        x1, y1, x2, y2 = canvas.coords(self.id)

        # Проверка столкновения с левой ракеткой
        if self.collides_with(player1):
            self.x_speed = -self.x_speed + 0.25
            score += 1
            canvas.itemconfig(score_gui, text=f"Счет: {score}")
            try:
                playsound('pong.mp3', block=False)
            except:
                pass

        # Проверка столкновения с правой ракеткой
        if self.collides_with(player2):
            self.x_speed = -self.x_speed - 0.25
            score += 1
            canvas.itemconfig(score_gui, text=f"Счет: {score}")
            try:
                playsound('pong.mp3', block=False)
            except:
                pass

        # Проверка столкновения со стенками
        if y1 <= 0 or y2 >= 600:
            self.y_speed *= -1
            try:
                playsound('ping.mp3', block=False)
            except:
                pass

        if x1 <= 0 or x2 >= 800:
            return True

        return False

    # Функция проверки столкновения мяча с ракеткой
    def collides_with(self, player):
        p_x1, p_y1, p_x2, p_y2 = canvas.coords(player.id) # координаты ракетки
        x1, y1, x2, y2 = canvas.coords(self.id) # координаты мяча
        return (y1 < p_y2 and y2 > p_y1 and ((x1 <= p_x2 and x2 >= p_x1) or (x2 >= p_x1 and x1 <= p_x2)))

# Цикл игры
def game_loop():
    loser = ball.draw()
    player1.draw()
    player2.draw()
    if loser:
        try:
            # Открываем файл рекордов и проверяем, побит ли текущий рекорд
            record_file = open("score.ini", "r+")
            current_record = int(record_file.readline())
            if current_record < score:
                record_file.truncate(0)
                record_file.seek(0)
            record_file.write(f"{score}")
            record_file.close()
        except:
            pass
        canvas.create_text(400, 300, text="Игра окончена!", fill="white", font=("Consolas", 30))
        return
    root.after(10, game_loop)

# При закрытии окна сохраняется текущий рекорд
def on_closing():
    try:
        # Сохранение рекорда при закрытии окна
        record_file = open("score.ini", "r+")
        current_record = int(record_file.readline())
        if current_record < score:
            record_file.truncate(0)
            record_file.seek(0)
            record_file.write(f"{score}")
        record_file.close()
    except:
        pass
    root.destroy()


# Создание объектов игры
player1 = Player1()
player2 = Player2()
ball = Ball()

# Привязка клавиш управления
root.bind_all("<KeyPress>", player1.move)
root.bind_all("<KeyPress>", player2.move, add="+")
root.bind_all("<KeyRelease>", player1.stop)
root.bind_all("<KeyRelease>", player2.stop, add="+")

# Обработка закрытия окна
root.protocol("WM_DELETE_WINDOW", on_closing)
game_loop()
root.mainloop()