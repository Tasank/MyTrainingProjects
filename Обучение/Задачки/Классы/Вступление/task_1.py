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
