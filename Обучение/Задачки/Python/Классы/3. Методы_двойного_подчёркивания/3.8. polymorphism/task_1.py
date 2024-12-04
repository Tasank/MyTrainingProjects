class Human:
    def __init__(self, name, age, gender='Мужской'):
        self.name = name
        self. age = age
        self.gender = gender

    def info(self):
        print(f'Вызывается метод info объекта класса Human. \n'
              f'ID - объекта человека: {id(self)} \n'
              f'Имя: {self.name}, возраст: {self.age}, пол: {self.gender}. \n')


class Student(Human):
    def __init__(self, speciality, name, age):
        super().__init__(name, age)
        self.speciality = speciality
    def info(self):
        print(f'Вызывается метод info объекта класса Student. \n'
              f'ID - объекта студента: {id(self)}. \n'
              f'Имя: {self.name}, специальность: {self.speciality}. \n')

class Book:
    def __init__(self, title):
        self.title = title

    def info(self):
        print(f'Вызывается метод info объекта класса Book. \n'
              f'ID - объекта книги: {id(self)}. \n'
              f'Название книги: {self.title}. \n')


Boris = Human('Борис', 25)
Eva = Student('Информатика', 'Ева', 19)
book = Book('Python ООП')

objects = [Boris, Eva, book]

for obj in objects:
    obj.info()