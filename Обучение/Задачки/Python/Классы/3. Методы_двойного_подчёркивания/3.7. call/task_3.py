"""
Напишите декоратор Logger, который будет записывать информацию о
вызываемой функции и ее аргументах в файл log.txt. Декоратор должен иметь возможность записывать
информацию о вызываемой функции в разных форматах (например, JSON или CSV).
"""
import json
import csv
import time

class Logger:
    def __init__(self, format='txt'):
        self.format = format

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            if self.format == 'txt':
                with open('log.txt', 'a') as file:
                    file.write(f"Function: {func.__name__}, Args: {args}, {kwargs}, Result: {result}, Execution Time: {execution_time:.6f} seconds\n")
            elif self.format == 'json':
                with open('log.txt', 'a') as file:
                    file.write(json.dumps({"function": func.__name__, "args": args, "kwargs": kwargs, "result": result, "execution_time": execution_time}) + "\n")
            elif self.format == 'csv':
                with open('log.txt', 'a', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=["function", "args", "kwargs", "result", "execution_time"])
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow({"function": func.__name__, "args": str(args), "kwargs": str(kwargs), "result": result, "execution_time": execution_time})

            return result
        return wrapper

@Logger(format='txt')
def add(a, b):
    return a + b

@Logger(format='json')
def add_json(a, b):
    return a + b

@Logger(format='csv')
def add_csv(a, b):
    return a + b


if __name__ == '__main__':
    add(2, 2)
    add_json(2, 4)
    add_csv(2, 4)