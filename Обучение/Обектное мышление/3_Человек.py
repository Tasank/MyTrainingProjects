class Human:
    def __init__(self, name: str, age: int, gender: str, height: int, weight: int, health: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.health = health

    def hello_me(self):
        print(f'Привет, меня зовут {self.name}')
        print(f'Мне - {self.age} лет')
        print(f'Я - {self.gender}')
        print(f'Мой рост - {self.height} см')
        print(f'Мой вес - {self.weight} кг')
        print(f'Моя здоровье - [{self.health}]', end='\n\n')

    def birthday(self):
        self.age += 1

    def do_it(self, func):
        print('Выполняю поставленную задачу')
        try:
            func()
            print('Задачу выполнил.')
        except Exception as e:
            print('Задача не выполнена.', e)


Alya = Human('Алия', 20, 'девушка', 170, 60, 'здорова')
Alya.hello_me()


def play():
    print('Пнуть мячик')


Alya.do_it(play)
