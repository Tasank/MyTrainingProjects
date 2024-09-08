from random import choice
from random import randint

class NPC:
    def __init__(self):
        self.gender = choice(['мужской', 'женский'])
        self.first_name, self.last_name = self.set_random_name()
        self.race = self.random_race()
        self.age = self.random_age()
        self.type_activity = self.random_activity()


    def set_random_name(self):
        first_name_boy_list = ['Иван', 'Петр', 'Александр', 'Василий', 'Максим']
        first_name_girl_list = ['Анастасия', 'Анна', 'Ольга', 'Мария', 'Екатерина']
        last_name_boy_list = ['Стяжкин', 'Гробовщиков', 'Жуков', 'Мельников', 'Тачксаков']
        last_name_girl_list = ['Звёздная', 'Плотникова', 'Кузнецова', 'Павлова', 'Савельева']
        if self.gender == 'мужской':
            self.first_name = choice(first_name_boy_list)
            self.last_name = choice(last_name_boy_list)
        elif self.gender == 'женский':
            self.first_name = choice(first_name_girl_list)
            self.last_name = choice(last_name_girl_list)
        return self.first_name, self.last_name

    def random_race(self):
        race_list = ['Человек', 'Эльф', 'Орк', 'Нежить', 'Дворф', 'Драконид', 'Зверолюд',]
        self.race = choice(race_list)
        return self.race

    def random_activity(self):
        activity_list = ['Спорт', 'Служба', 'Охота', 'Работа', 'Своё дело', 'Кулинария', 'Игры', 'Учёба']
        self.type_activity = choice(activity_list)
        return self.type_activity

    def random_age(self):
        if self.race == 'Человек':
            self.age = randint(10, 110)
        elif self.race == 'Эльф':
            self.age = randint(10, 700)
        elif self.race == 'Орк':
            self.age = randint(10, 80)
        elif self.race == 'Нежить':
            self.age = 'неизвестен'
        elif self.race == 'Дворф':
            self.age = randint(10, 300)
        elif self.race == 'Драконид':
            self.age = randint(10, 1100)
        elif self.race == 'Зверолюд':
            self.age = randint(10, 210)
        return self.age

    def __str__(self):
        return (f'Имя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: '
                f'{self.age}\nПол: {self.gender}\nВид действия: {self.type_activity}\nРаса: {self.race}'
                f'\n___________________')

npc_1 = NPC()
npc_2 = NPC()
npc_3 = NPC()

print(npc_1)
print(npc_2)
print(npc_3)