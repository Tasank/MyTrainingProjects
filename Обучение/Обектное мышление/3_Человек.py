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
        print(f'Моя здоровье - [{self.health}]')

Alya = Human('Алия', 20, 'девушка', 170, 60, 'здорова')
Alya.hello_me()