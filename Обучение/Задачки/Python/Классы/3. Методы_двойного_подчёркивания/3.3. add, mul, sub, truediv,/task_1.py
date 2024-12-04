# Класс который складывает символы

class Adder:
    def __init__(self, txt):
        self.txt = txt
    # Определяем метод сложения
    def __add__(self, other):
        print('Вызван метод __add__')
        if other is None:
            print('Нельзя сложить пустую строку')
            return
        print(f'Символы {self.txt} и {other} складываются')
        return self.txt + other
    #
    def __radd__(self, other):
        print('Вызван метод __radd__')
        if other is None:
            print('Нельзя сложить пустую строку')
            return
        return other + self.txt

txt = Adder('abc')
result = txt + '123' # Python вызывает метод __add__ у объекта txt, потому что txt находится в левой части оператора (+)
print(result)

result = '123' + txt # Когда мы пишем '123' + txt, Python вызывает метод __radd__ у объекта txt, потому что txt находится в правой части оператора
print(result)
