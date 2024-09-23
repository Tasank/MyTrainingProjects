"""
Класс "Матрица": Создайте класс MyMatrix,
который хранит матрицу и имеет метод __abs__,
который возвращает определитель матрицы.

Класс "Дата": Создайте класс MyDate,
который хранит дату и имеет метод __abs__,
который возвращает количество дней между датой и текущей датой.
"""

class MyMatrix:
    def __init__(self):
        self.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def __abs__(self):
        # Возвращаем определитель матрицы
        # Определитель матрицы это первый элемент первого столбца
        # 1 * 5 * 9
        return self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]

    def __str__(self):
        return f'{self.matrix}'

matrix = MyMatrix()
print(abs(matrix))

class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __abs__(self):
        # Возвращаем количество дней между датой и текущей датой
        return abs((2023 - self.year) * 365 + (12 - self.month) * 30 + (30 - self.day))

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

date = MyDate(10, 11, 2022)
print(abs(date))