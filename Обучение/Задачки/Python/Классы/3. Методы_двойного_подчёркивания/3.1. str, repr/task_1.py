

class MyClass:
    def __init__(self):
        self.info = 'Это атрибут'

    def __str__(self):
        return f'В классе есть {self.info}'

    def __repr__(self):
        return f'Это вывод для разработчиков'

polo = MyClass()

print(polo)
print(repr(polo))
