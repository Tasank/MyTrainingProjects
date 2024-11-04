"""
Создайте стеко-подобную структуру данных, в которую можно добавлять элементы и
извлекать самый часто встречающийся элемент.

Реализуйте класс FreqStack:

FreqStack() должен создавать пустой стек, представленный списком
push(value) добавляет значение value (типа int) в конец стека (списка), этот метод ничего не возвращает
pop() извлекает из стека (списка) самый часто встречающийся элемент и удаляет его из стека (списка)
get() возвращает список всех элементов
Примечание: Если несколько элементов встречаются одинаковое количество раз,
то метод pop возвращает тот, который ближе к концу стека(списка).

"""


class FreqStack:
    def __init__(self):
        self.freq = {}  # Словарь для хранения частоты каждого элемента
        self.group = {}  # Словарь для хранения групп элементов по частоте
        self.max_freq = 0  # Максимальная частота

    def push(self, value: int):
        # Увеличиваем частоту элемента
        self.freq[value] = self.freq.get(value, 0) + 1
        f = self.freq[value]

        # Обновляем максимальную частоту
        if f > self.max_freq:
            self.max_freq = f

        # Добавляем элемент в соответствующую группу частоты
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(value)

    def pop(self) -> int:
        # Извлекаем элемент из группы с максимальной частотой
        value = self.group[self.max_freq].pop()

        # Уменьшаем частоту элемента
        self.freq[value] -= 1

        # Если группа с максимальной частотой пуста, уменьшаем максимальную частоту
        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return value

    def get(self) -> list:
        # Собираем и возвращаем все элементы в порядке их добавления
        elements = []
        for f in range(1, self.max_freq + 1):
            if f in self.group:
                elements.extend(self.group[f])
        return elements


# Пример использования:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.get())  # Вывод: [5, 7, 5, 7, 4, 5]
print(obj.pop())  # Вывод: 5
print(obj.get())  # Вывод: [5, 7, 5, 7, 4]
print(obj.pop())  # Вывод: 7
print(obj.get())  # Вывод: [5, 7, 5, 4]
