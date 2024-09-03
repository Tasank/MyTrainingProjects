"""
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(),
выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза:
Обычная газировка.
"""
class Soda:
    # @param grad = Это добавка по умолчанию она равна None
    # @return Возвращает добавку или None
    def __init__(self, grad=None):
        if isinstance(grad, str):
            self.grad = grad
        else:
            self.grad = None

    def show_my_drink(self):
        if self.grad:
            print(f'Газировка и добавка ({self.grad}) ')
        else:
            print('Обычная газировка.')
# Объявление объектов
first = Soda()
second = Soda(10)
biblomb = Soda('Голубика')
# Вывод
first.show_my_drink()
second.show_my_drink()
biblomb.show_my_drink()


