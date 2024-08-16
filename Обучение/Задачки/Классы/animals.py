"""Классы животных"""
# Определения класса
class Dog:
    def __init__(self, age, name):
        # Атрибуты объекта
        self.age = age
        self.name = name
    # Метод класса
    def hungry(self):
        print(f'{self.name}: Уаф! РРррр! Грр! Уав! Уаф! Оуу? Ууууу( ')

# Создание объектов класса
one_dog = Dog(3, 'Boby')
two_dog = Dog(2, 'Crazy')

# Доступ к атрибутам
print(f' Возраст собаки: {two_dog.age}')

# Вызов методов
two_dog.hungry()
