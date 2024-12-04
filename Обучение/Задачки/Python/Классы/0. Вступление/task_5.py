class Technic:
    # Атрибуты класса
    name = 'Компьютер'
    price = 5000
    energy = 13

    # Метод класса
    def buy(self):
        print(f'Вы купили {self.name} по цене ({self.price}).\n')

    # Метод класса
    def info(self):
        print(f'{self.name} цена: {self.price}, энергия: {self.energy}\n')


# объект класса
# Тест_1
computer = Technic()
computer.info()


# обращение к атрибуту через класс или объект класса
# Тест_2
print('Цена компьютера: ', Technic.price)
print('Название компьютера: ', computer.name)

# вызов ф-ии через класс
# Тест_3
Technic.buy(computer)
getattr(Technic, 'buy')(computer)

# создание и изменение значения атрибута
# Тест_4
Technic.price = 10000
Technic.color = 'blue'
setattr(Technic, 'weight', '5 кг')


# удаление атрибута
# Тест_5
del Technic.color
delattr(Technic, 'weight')

# посмотреть атрибуты класса или объект класса
# Тест_6
print(Technic.__dict__)
print(computer.__dict__)