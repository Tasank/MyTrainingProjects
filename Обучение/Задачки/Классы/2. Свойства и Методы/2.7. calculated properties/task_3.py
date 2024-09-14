"""
Задание 3: Создайте класс Student с вычисляемым свойством average_grade,
которое вычисляет средний балл студента на основе списка оценок.

Требования:

Класс Student должен иметь метод add_grade(grade), который добавляет новую оценку в список.
Calculated property average_grade должно вычислять средний балл студента,
используя метод sum() и количество оценок.
Создайте экземпляр класса Student и добавьте несколько оценок.
Выведите средний балл студента.
"""

class Student:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade): # Добавить оценку в список
        self.grades.append(grade)

    @property
    def average_grade(self): # Средняя оценка
        return sum(self.grades) / len(self.grades)

stiven = Student()
stiven.add_grade(5)
stiven.add_grade(4)
stiven.add_grade(3)
print(f'Средняя оценка: {stiven.average_grade}')
