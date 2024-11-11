"""
Создайте класс Vector, который хранит в себе список чисел.
Реализуйте методы __getitem__, __setitem__ и __delitem__,
чтобы можно было работать с числами в векторе как с элементами списка.
"""

class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Только индексы целочисленного типа')
        elif item < 0 or item >= len(self.values):
            raise IndexError('Индекс за границами Вектора')
        else:
            print(f'Элемент с индексом {item} равен {self.values[item]}')
            return self.values[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Ошибка установки значения. Только индексы целочисленного типа')
        elif key < 0 or key >= len(self.values):
            raise IndexError('Ошибка установки значения. Индекс за границами Вектора')
        elif key < 0:
            raise IndexError('Ошибка установки значения. Индекс меньше нуля')
        elif key > len(self.values):
            print(f'Добавлено {key - len(self.values)} элементов')
            diff = key - len(self.values)
            self.values.extend([0] * diff)
        print(f'Элемент с индексом {key} установлен на {value}')
        self.values[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Ошибка удаления значения. Только индексы целочисленного типа')
        elif key < 0 or key >= len(self.values):
            raise IndexError('Ошибка удаления значения. Индекс за границами Вектора')
        else:
            print(f'Элемент с индексом {key} удален его значение {self.values[key]}')
            del self.values[key]

    def __repr__(self):
        return str(self.values)

v = Vector(1, 2, 3)
print(v[0])  # выведет 1,
v[1] = 4
print(v[1])  # выведет 4
del v[2] # удалить элемент с индексом 2 (3-й элемент)
print(v)  # выведет [1, 4]