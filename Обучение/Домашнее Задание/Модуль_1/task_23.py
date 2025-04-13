
if by <= y11 and by1 >= y1 and bx <= x11:
    self.x = abs(self.x)
    player1.speed += 0.25  # Увеличиваем скорость первого игрока
    self.x += 0.25 # Здесь увеличиваем скорость
    score += 1
    canvas.itemconfig(score_gui, text=f"Счёт: {score}")


if by <= y22 and by1 >= y2 and bx1 >= x2:
    self.x = -abs(self.x)
    player2.speed += 0.25 # Увеличиваем скорость второго игрока
    self.x -= 0.25
    score += 1
    canvas.itemconfig(score_gui, text=f"Счёт: {score}")
