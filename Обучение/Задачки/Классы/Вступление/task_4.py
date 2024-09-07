class Human:
    # Атрибуты класса
    name = 'Вася'
    age = 25
    gender = 'мужской'

    # Метод класса
    def info(self):
        print(f'Имя: {self.name}, возраст: {self.age}, пол: {self.gender}.')
        print()
    def birthday(self):
        self.age += 1
        print(f'С день рождения {self.name}! Теперь тебе: {self.age}')
        print()

# экземпляр класса
# Тест_1
human = Human()
human.info()


# обращение к атрибуту через класс или экземпляр
# Тест_2
print(Human.age)
print(human.name)


# вызов ф-ии через класс
# Тест_3
Human.birthday(human)
getattr(Human, 'birthday')(human)

# создание и изменение значения атрибута
# Тест_4
Human.name = 'Петя'
Human.height = 150
setattr(Human, 'weight', 70)

# удаление атрибута
# Тест_5
del Human.weight
delattr(Human, 'height')

# посмотреть атрибуты класса или экземпляра
# Тест_6
print(Human.__dict__)
print(human.__dict__)