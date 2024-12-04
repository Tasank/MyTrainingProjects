"""
Создайте класс Countdown, который будет итерируемым и позволит вам выполнять обратный отсчет
от заданного числа до 1 использовать __iter__ и __next__, чтобы сделать объект итерируемым.
"""
import time
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 1:
            raise StopIteration
        else:
            self.start -= 1
            time.sleep(1)
            return self.start

for i in Countdown(6):
    print(i)
