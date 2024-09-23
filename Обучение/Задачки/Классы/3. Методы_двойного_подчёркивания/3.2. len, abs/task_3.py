"""
Класс "Множество": Создайте класс MySet, который хранит множество элементов и имеет метод __len__,
который возвращает количество элементов в множестве.
"""
class MySet:
    def __init__(self):
        self.elements = []
    # Метод добавления элемента в множество
    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
    # Метод для вычисления длины множества
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            print('Такого элемента нет в множестве.')
    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)


my_set = MySet()
my_set.add(1)
my_set.add('Второй элемент')
my_set.add(2)
my_set.add(3)

print(my_set) # [1, 'Второй элемент', 2, 3]
my_set.remove('Второй элемент')
print(my_set) # [1, 2, 3]

print(my_set.__len__()) # 3