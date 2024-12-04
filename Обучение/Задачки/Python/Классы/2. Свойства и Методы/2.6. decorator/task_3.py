"""
Задача 3: Напишите декоратор, который будет добавлять к результату функции строку "Результат: ".
Используйте декоратор для функции, которая возвращает строку "Привет, мир!".
"""
def result_decorator(func):
    def wrapper():
        result = func()
        return "Результат: " + str(result)
    return wrapper

@result_decorator
def my_func():
    return "Привет, мир!"

print(my_func())
