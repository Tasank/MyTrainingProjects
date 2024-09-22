"""
Создайте класс MyString, который хранит строку и имеет метод __len__, который возвращает длину строки.
"""

class MyString:
    def __init__(self, string):
        self.string = string
    def __len__(self):
        return len(self.string)


text = MyString("Hello, World!")
print(len(text))
print(text.__len__())
