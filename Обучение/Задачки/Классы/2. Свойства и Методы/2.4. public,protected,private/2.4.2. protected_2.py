class Cat:
    def __init__(self, name, age, speak='Мяу'):
        self._name = name
        self._age = age
        self._speak = speak

    def info(self):
        print(f"Имя кота: {self._name}. Возраст: {self._age}")

    def make_sound(self):
        print("Говорит:", self._speak)

cat = Cat("Барсик", 5)
cat.info()
cat.make_sound()
print(cat._name)