"""
Итератор (iterator) - это объект, который может быть использован для последовательного доступа к элементам коллекции
(например, списка, словаря или набора данных) без необходимости загружать все элементы в память одновременно.

Итераторы позволяют выполнять операции, такие как итерация (перебор) элементов, фильтрация, преобразование,
объединение и т. д., над коллекцией без необходимости загружать все элементы в память.
"""
# Класс Move представляет собой набор элементов, которые можно итерировать
class Move:
    # Инициализация объекта Move с произвольным количеством аргументов
    def __init__(self, *args):
        self.args = args

    # Свойство elements возвращает итератор по элементам Move
    @property
    def elements(self):
        # Использование yield для ленивой итерации по элементам
        for i in self.args:
            yield i

    # Метод add_element добавляет новый элемент в Move
    def add_element(self, element):
        # Добавление элемента в конец списка args
        self.args += (element,)

    # Метод remove_element удаляет элемент из Move
    def remove_element(self, element):
        # Проверка наличия элемента в args
        if element in self.args:
            # Удаление элемента из args
            self.args = tuple(arg for arg in self.args if arg != element)
        else:
            # Вывод сообщения об отсутствии элемента
            print(f"Элемент {element} не найден в Move")

    # Метод clear_elements очищает все элементы Move
    def clear_elements(self):
        # Очистка списка args
        self.args = ()

    # Метод __str__ возвращает строковое представление Move
    def __str__(self):
        # Вывод строкового представления Move
        return f"Move({', '.join(map(str, self.args))})"

# Создание объекта Move
move = Move(1, 2, 3)

# Вывод элементов Move
print("Элементы Move:")
for elem in move.elements:
    print(elem)

# Добавление нового элемента в Move
move.add_element(4)
print("\nЭлементы Move после добавления:")
for elem in move.elements:
    print(elem)

# Удаление элемента из Move
move.remove_element(2)
print("\nЭлементы Move после удаления:")
for elem in move.elements:
    print(elem)

# Очистка всех элементов Move
move.clear_elements()
print("\nЭлементы Move после очистки:")
for elem in move.elements:
    print(elem)

# Вывод строкового представления Move
print("\nСтроковое представление Move:")
print(move)