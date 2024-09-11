class Cat:
    def __init__(self, name, age, speak='Мяу'):
        self.name = name
        self.age = age
        self.speak = speak

    def info(self):
        print(f"Имя кота: {self.name}. Возраст: {self.age}")

    def make_sound(self):
        print("Говорит:", self.speak)

cat = Cat("Барсик", 5)
cat.info()
cat.make_sound()
