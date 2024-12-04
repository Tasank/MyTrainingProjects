import time
def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Время выполнения функции: {end_time - start_time} секунд")
        return wrapper
@timer_decorator
def my_func():
    time.sleep(1)
    print('Работа функции')

my_func()