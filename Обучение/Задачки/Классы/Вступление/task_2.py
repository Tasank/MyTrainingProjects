class Weapon:
    # Атрибуты класса
    name = 'Ракета'
    damage = 1000

    # Метод класса
    def attack(self, target):
        print(f'{self.name} поразила цель ({target}).\n({target}): уничтожен.')


# экземпляр класса
# Тест_1
rocket = Weapon()
rocket.attack('пушка')
print()

# обращение к атрибуту через класс или экземпляр
# Тест_2
print('Урон класса "Оружие" по умолчанию: ', Weapon.damage)
print('Название объекта класса "Оружие" по умолчанию:', rocket.name)
print()

# вызов ф-ии через класс
# Тест_3
Weapon.attack(rocket, 'Абрамс')
getattr(Weapon, 'attack')(rocket, 'Абрамс')
print()

# создание и изменение значения атрибута
# Тест_4
Weapon.damage = 3400
Weapon.new_range = '50 км'
setattr(Weapon, 'speed_rate', 1)
print('Новый урон: ', Weapon.damage)
print('Новый атрибут {new_range}, значение: ', Weapon.new_range)
print('Новый атрибут {speed_rate}, значение: ', Weapon.speed_rate)
print()

# удаление атрибута
# Тест_5
del Weapon.speed_rate
delattr(Weapon, 'new_range')
print('Проверка.')
try:
    print('Новый атрибут {speed_rate}, значение: ', Weapon.speed_rate)
except AttributeError:
    print('Атрибут {speed_rate} удален')
    print()

# посмотреть атрибуты класса или экземпляра
# Тест_6
print(Weapon.__dict__)
print(rocket.__dict__)