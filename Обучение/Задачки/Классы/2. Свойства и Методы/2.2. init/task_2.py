from random import randint

class Warrior:
    def __init__(self, name):
        self.name = name
        self.stamina = self.defining_characteristics()
        self.strength = self.defining_characteristics()
        self.agility = self.defining_characteristics()

    def defining_characteristics(self):
        return randint(1, 10)

    def train(self, name):
        if name == "выносливость":
            self.stamina += 1
            print(f'Выносливость после тренировки: {max.stamina}')
        elif name == "сила":
            self.strength += 1
            print(f'Сила после тренировки: {max.strength}')
        elif name == "ловкость":
            self.agility += 1
            print(f'Ловкость после тренировки: {max.agility}')


    def __str__(self):
        return (f'Имя: {max.name} \n - выносливость: {self.stamina} \n - сила: {self.strength} \n -'
                f' ловкость: {self.agility}')

max = Warrior("Максим")
print(max, '\n')
print(f'Имя: {max.name}')
print(f'Начальная сила: {max.strength}')

max.train("сила")
