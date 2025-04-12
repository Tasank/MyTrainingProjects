from tkinter import *

root = Tk()
root.geometry('800x600')
root.title('Ping-Pong')

canvas = Canvas(root, width=800, height=600, bg='black')
canvas.pack()

class Player:
    def __init__(self):
        self.id = None
        self.y = None

    def draw(self):
        canvas.move(self.id, 0, self.y)
        _, y, _, y1 = canvas.coords(self.id)
        if y <= 0 or y1 >= 600:
            self.y = 0

class Player1(Player):
    def __init__(self):
        super().__init__()
        self.id = canvas.create_rectangle(10, 10, 20, 90, fill='white')
        self.y = 0
        self.speed = 3

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
        self.id = canvas.create_rectangle(770, 10, 780, 90, fill='white')
        self.y = 0
        self.speed = 3

    def move(self, event):
        if event.keysym == 'Up':
            self.y = -self.speed
        if event.keysym == 'Down':
            self.y = self.speed

    def stop(self, event):
        if event.keysym in ("Up", "Down"):
            self.y = 0

player1 = Player1()
player2 = Player2()

root.bind_all('<KeyPress-w>', player1.move)
root.bind_all('<KeyPress-s>', player1.move)
root.bind_all('<KeyRelease-w>', player1.stop)
root.bind_all('<KeyRelease-s>', player1.stop)

root.bind_all('<KeyPress-Up>', player2.move)
root.bind_all('<KeyPress-Down>', player2.move)
root.bind_all('<KeyRelease-Up>', player2.stop)
root.bind_all('<KeyRelease-Down>', player2.stop)

def game_loop():
    player1.draw()
    player2.draw()
    root.after(16, game_loop)

game_loop()
root.mainloop()
