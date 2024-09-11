class Cat:
    def __init__(self, name, age, speak='Мяу'):
        self.__name = name
        self.__age = age
        self.__speak = speak

    def info(self):
        print(f"Имя кота: {self.__name}. Возраст: {self.__age}")

    def __make_sound(self):
        print("Говорит:", self.__speak)

cat = Cat("Барсик", 5)
cat.info()
cat._Cat__make_sound() # через класс можем вызвать приватный метод
print(cat._Cat__name) # через класс можем вызвать приватный атрибут