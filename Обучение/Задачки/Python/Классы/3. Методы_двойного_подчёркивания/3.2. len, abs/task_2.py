"""
Класс "Список": Создайте класс MyList, который хранит список элементов и имеет метод __len__,
который возвращает количество элементов в списке.
"""

class MyList:
    def __init__(self, li):
        self.li = li

    def __len__(self):
        return len(self.li)

my_list = MyList([1, 2, 3, 4, 146, 'doma'])
print(len(my_list))
print(my_list.__len__())
