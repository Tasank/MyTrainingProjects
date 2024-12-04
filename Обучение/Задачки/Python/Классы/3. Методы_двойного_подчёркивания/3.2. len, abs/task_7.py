"""
Класс "Контейнер", который хранит коллекцию элементов
и имеет методы __len__ и __abs__, которые возвращают
длину коллекции и абсолютное значение коллекции соответственно.


Класс "Число", который хранит число и имеет методы __len__ и __abs__,
которые возвращают количество цифр в числе и абсолютное значение
числа соответственно.
"""
class Container:
    def __init__(self, collection):
        self.collection = collection

    def __len__(self):
        return len(self.collection)

    def __abs__(self):
        return abs(sum(self.collection))

class Number:
    def __init__(self, num):
        self.num = num

    def __len__(self):
        return len(str(self.num))

    def __abs__(self):
        return abs(self.num)


container = Container([1, 2, 3, 4, 5])
print(len(container)) # 5
print(abs(container)) # 15

print()

number = Number(-10)
print(len(number)) # 3 т.к. минус тоже учитывается
print(abs(number)) # 10