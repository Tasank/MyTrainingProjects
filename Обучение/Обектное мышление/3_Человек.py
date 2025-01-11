class Human:
    def __init__(self, name: str, age: int, gender: str, height: int, weight: int, health: str):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.health = health

        gender_list = ['мужской', 'женский']
        if gender.lower() in gender_list:
            self.gender = gender
        else:
            self.gender = 'мужской'

        self.povestka()

    def hello_me(self):
        print(f'Привет, меня зовут {self.name}')
        print(f'Мне - {self.age} лет')
        print(f'Я - {self.gender}')
        print(f'Мой рост - {self.height} см')
        print(f'Мой вес - {self.weight} кг')
        print(f'Моя здоровье - [{self.health}]', end='\n\n')

    def povestka(self):
        if self.gender == 'мужской' and self.age >= 18:
            print('Пришла повестка')

    def birthday(self):
        self.age += 1

    def do_it(self, func):
        print('Выполняю поставленную задачу')
        try:
            func()
            print('Задачу выполнил.')
        except Exception as e:
            print('Задача не выполнена.', e)


Alya = Human('Алия', 20, 'женский', 170, 60, 'здорова')
Alya.hello_me()


def play():
    print('Пнуть мячик')


Alya.do_it(play)
