"""
Создайте класс "Учитель" и определите функцию "преподавать".
Затем, создайте объект класса "Учитель" и вызовите функцию.
"""

# 4 вариант: обращения через @classmethod, @staticmethod
class Teacher:
    book = 'Python'
    @classmethod
    def teach(cls):
        print(f"Учитель преподает {cls.book}")

    @staticmethod
    def teach_other():
        print(f"Учитель преподаёт {Teacher.book}")


human = Teacher()
human.teach()
human.teach_other()
