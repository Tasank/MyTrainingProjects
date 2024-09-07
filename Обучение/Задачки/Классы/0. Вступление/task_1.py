class Food:
    # Атрибуты класса
    name = 'Пицца'
    size = 2
    # Метод класса
    def eat(name, size):
        print('Кусь*')
        # Размер <__main__.Food object at 0x000001B300618290> равняется 1
        print(f'Размер {name} равняется {size}')

    def close_eat():
        print('Я поел')

# экземпляр класса
# Тест_1
pizza = Food()
pizza.eat(1)
print()

# обращение к атрибуту через класс или экземпляр
# Тест_2
print(Food.size)
print(pizza.name)

# вызов ф-ии через класс
# Тест_3
Food.close_eat()
getattr(Food, 'close_eat')()
print()

# создание и изменение значения атрибута
# Тест_4
Food.name = 'Колбаса'
Food.new_attribute = 'creation_new_attribute'
setattr(Food, 'new_attr', 'change_new_attr')
print(Food.new_attribute)
print(Food.new_attr)
print()

# удаление атрибута
# Тест_5
del Food.new_attribute
delattr(Food, 'new_attr')

# посмотреть атрибуты класса или экземпляра
# Тест_6
print(Food.__dict__)
print(pizza.__dict__)
