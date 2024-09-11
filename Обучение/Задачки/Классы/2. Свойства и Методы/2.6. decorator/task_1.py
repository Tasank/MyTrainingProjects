def my_decorator(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

@my_decorator
def my_function():
    print("Вызов функции")

my_function()