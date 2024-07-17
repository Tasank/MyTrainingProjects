"""
Упражнение 12. Расстояние между точками на Земле.
Напишите программу, в которой пользователь будет вводить координаты двух точек на Земле (широту и долготу) в градусах.
На выходе мы должны получить расстояние между этими точками при следовании по кратчайшему пути по поверхности планеты.
"""
import math


def calculate_distance(lat1, lon1, lat2, lon2):
    # Переводим градусы в радианы
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Используем формулу для вычисления расстояния
    distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) +
                                   math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
    return distance


# Ввод координат
lat1 = float(input("Введите широту первой точки: "))
lon1 = float(input("Введите долготу первой точки: "))
lat2 = float(input("Введите широту второй точки: "))
lon2 = float(input("Введите долготу второй точки: "))

# Вычисление и вывод расстояния
distance = calculate_distance(lat1, lon1, lat2, lon2)
print(f"Расстояние между точками: {distance:.2f} км")
