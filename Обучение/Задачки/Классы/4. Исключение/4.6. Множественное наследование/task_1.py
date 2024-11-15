"""
Создайте класс Animal с атрибутами name и age. Создайте класс Mammal с атрибутом fur.
Создайте класс Carnivore с атрибутом teeth.
Используйте множественное наследование для создания класса Lion,
который наследует от классов Mammal и Carnivore.
"""
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mammal:
    def __init__(self, fur):
        self.fur = fur

class Carnivore:
    def __init__(self, teeth):
        self.teeth = teeth

class Lion(Animal, Mammal, Carnivore):
    def __init__(self, name, age, fur, teeth):
        Animal.__init__(self, name, age)
        Mammal.__init__(self, fur)
        Carnivore.__init__(self, teeth)

    def __repr__(self):
        return f'Лев: {self.name}, Возраст: {self.age}, Шерсть: {self.fur}, Зубы: {self.teeth}'


lion = Lion('Рыжик', 5, 'Длинная', 20)
print(lion)