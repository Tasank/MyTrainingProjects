"""
Класс "Словарь": Создайте класс MyDict, который хранит словарь ключ-значение и имеет метод __len__,
который возвращает количество пар ключ-значение в словаре.
"""
class MyDict:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict[key] = value

    def __len__(self):
        print(f"Количество пар ключ-значение в словаре: {len(self.dict)}")


my_dict = MyDict()
key = input('Введите ключ: ')
value = input('Введите значение: ')
my_dict.add(key, value)

my_dict.__len__()