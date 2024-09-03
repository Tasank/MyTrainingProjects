"""
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
"""
class TriangleChecker:
    def __init__(self, num):
        self.num = num
    # @return возвращаются следующие значения (в зависимости от ситуации):
    # – Ура, можно построить треугольник!;
    # – С отрицательными числами ничего не выйдет!;
    # – Нужно вводить только числа!;
    # – Жаль, но из этого треугольник не сделать.
    def is_triangle(self):
        # Если все числа относятся к типу (int или float)
        if all(isinstance(num,(int, float)) for num in self.num):
            # Если все числа больше 0
            if all(num > 0 for num in self.num):
                # Сортируем
                sorted_num = sorted(self.num)
                # Если сумма двух сторон больше максимально большой стороны
                if sorted_num[0] + sorted_num[1] > sorted_num[2]:
                    return 'Ура, можно построить треугольник!'
                else:
                    return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'

triangle_1 = TriangleChecker('1')
print(triangle_1.is_triangle())

triangle_2 = TriangleChecker([1, 2, 1])
print(triangle_2.is_triangle())

triangle_3 = TriangleChecker([5, 6, 3])
print(triangle_3.is_triangle())

triangle_3 = TriangleChecker([-6, -6, -6])
print(triangle_3.is_triangle())

