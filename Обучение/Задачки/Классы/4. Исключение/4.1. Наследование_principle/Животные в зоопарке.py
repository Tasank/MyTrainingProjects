"""
В зоопарке есть разные животные, у каждого из которых есть свои уникальные свойства и поведения.
Создайте класс Animal с методами eat(), sleep() и make_sound(). Затем создайте классы Mammal, Bird и Reptile,
которые наследуют свойства и методы класса Animal. Добавьте специфичные методы для каждого класса, например,
Mammal может иметь метод hunt(), Bird - fly(), а Reptile - shed_skin().
"""


class Animal:
    def eat(self):
        pass

    def sleep(self):
        print('Сплю в ночное время')

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, type='хищник'):
        if type == 'хищник':
            self.type = type
        else:
            self.type = 'травоядный'

        if self.type == 'хищник':
            self.hunt = self._hunt

    def eat(self):
        if self.type == 'хищник':
            print('Я ем мясо')
        else:
            print('Я ем траву')

    def _hunt(self, prey):
        print(f'Начинаю охоту на "{prey}"')


    def make_sound(self):
        print('Ррррр')


class Bird(Animal):
    def fly(self):
        print('Я могу летать')

    def make_sound(self):
        print('Чрик-чи-чик')


class Reptile(Animal):
    def shed_skin(self):
        print('Я могу снять кожу')


pantera = Mammal()

cow = Mammal('корова')
cow.eat()

pantera.eat()
pantera._hunt('крыса')

bird = Bird()
bird.fly() # Я могу летать
bird.sleep() # Сплю в ночное время
bird.eat() # None (т.к. метод не определён для этого подкласса)
