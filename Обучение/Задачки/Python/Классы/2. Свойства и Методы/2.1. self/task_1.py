class Rob:
    type_bot = 'Транспортировщик'
    # Метод класса, который принимает любое количество аргументов и печатает строку
    def hello(*args):
        # Печать строки с переданными аргументами
        print('Hello world. Я робот', args)

    # Метод класса, который печатает строку с видом робота
    def show_type(self):
        print(f'Я - {self.type_bot}')

    # Метод класса, который печатает строку с именем робота, если оно существует
    def show_name(self):
        if hasattr(self, 'name'):
            print(f'Меня зовут {self.name}')
        else:
            print('Такого нет')

    # Метод класса, который устанавливает атрибуты value и age робота
    def set_value(self, value, age=0):
        self.value = value
        self.age = age
        print(f'Мои значения: {self.value} и {self.age}')

    # Метод класса, который печатает сам робот
    def new_method(self):
        print(self)

# Создание экземпляра класса Rob
N1 = Rob()
# Вызов метода hello с аргументами
N1.hello('Терминатор', 'Уборщик', 'Проверщик')
# Вызов метода show_type
N1.show_type()
# Вызов метода show_name
N1.show_name()
# Вызов метода set_value
N1.set_value('loj', 1)
# Вызов метода new_method
N1.new_method()

