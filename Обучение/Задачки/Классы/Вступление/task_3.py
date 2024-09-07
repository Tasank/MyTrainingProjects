class Star:
    # Атрибуты класса
    name = 'Солнце'
    letter = '10 миллионов лет'

    # Метод класса
    def show(self):
        print(f'Звезде [{self.name}] сейчас - [{self.letter}]')
        print()

# экземпляр класса
# Тест_1
star = Star()
star.show()


# обращение к атрибуту через класс или экземпляр
# Тест_2
print(Star.name)
print(star.letter)

# вызов ф-ии через класс
# Тест_3
Star.show(star)
getattr(Star, 'show')(star)

# создание и изменение значения атрибута
# Тест_4
Star.name = 'Звезда Барнарда'
Star.size = 3
setattr(Star, 'color', 'красный')


# удаление атрибута
# Тест_5
del Star.color
delattr(Star, 'size')

# посмотреть атрибуты класса или экземпляра
# Тест_6
print(Star.__dict__)
print(star.__dict__)