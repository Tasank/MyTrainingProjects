class Phenomenon:
    name = 'Гравитация'

    # Метод класса, который принимает любое количество аргументов и печатает строку
    def hello(*args):
        print('Здравствуй(те):', args, '\n')

    # Метод класса, который печатает строку с атрибутом
    def show_type(self):
        print(f'Это - {self.name}\n')

    # Метод класса, который печатает строку с атрибутом, если оно существует
    def show_definition(self):
        if hasattr(self, 'name'):
           print(f'Определяемое нами является {self.name}\n')
        else:
           print('Такого нет\n')

    # Метод класса, который устанавливает атрибут variable
    def set_variables(self, variable):
        self.variable = variable
        print(f'Мы установили значение: {self.variable}\n')

    # Метод класса, который печатает сам себя
    def new_method(self):
        print(self)

# Создание объекта класса Phenomenon
it = Phenomenon()
it.hello('Буква', 'Янтарь', 'Водяной', 'Начать')
it.show_type()
it.show_definition()
it.set_variables(3.14)
it.new_method()