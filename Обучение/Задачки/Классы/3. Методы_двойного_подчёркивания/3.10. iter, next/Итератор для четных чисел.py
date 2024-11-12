"""
Создайте класс EvenNumbers, который будет итерируемым и будет генерировать четные числа,
начиная с 0 и до заданного предела  __iter__ и __next__.

Подсказка: Убедитесь, что итератор возвращает только четные числа и
завершает работу после достижения заданного предела.
"""


class EvenNumbers:
    def __init__(self, end):
        self.end = end
        self.current = 0

    def __iter__(self):
        print('Начинается итерация.')
        return self

    def __next__(self):
        if self.current <= self.end:
            if self.current % 2 == 0:
                result = self.current
                self.current += 2
                return result
            self.current += 1
        else:
            raise StopIteration

for i in EvenNumbers(10):
    print(f'Чётное - {i}')
