"""
Создайте новый класс NewFloat, который наследуется от float. Добавьте метод round_to,
который позволяет округлить число до заданного количества знаков после запятой.
"""

class NewFloat(float):
    def round_to(self, count):
        return round(self, count)

num = NewFloat(3.14159)
print(num) # 3.14159
print(num.round_to(2)) # 3.14

num_2 = 3.14159
print(round(num_2, 2)) # 3.14