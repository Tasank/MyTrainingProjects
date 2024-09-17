"""
Создайте класс "Автомобиль" и определите переменные "марка", "модель" и "год выпуска".
Затем, создайте объект класса "Автомобиль" и вызовите переменные.
"""
# 1 вариант: обращения через self

class Car:
    marca = 'Nissan'
    model = 'X-trail'
    year = 2022

    def make_car(self):
        print(f'Марка: {self.marca}, модель: {self.model}, год выпуска: {self.year}')

my_car = Car()
print(my_car.model)
my_car.make_car()
