"""
Множества - это неупорядоченные коллекции уникальных элементов.

Множества не могут содержать повторяющиеся элементы.
Множества не поддерживают индексирование.
Множества не поддерживают срезы.
Множества не поддерживают дубликаты.
"""

example_set = {1, 2, 3, 4, 5}
print(*example_set)

example_set.add(6)
print(*example_set)

example_set.remove(3)
print(*example_set)

example_set.clear()
print(example_set) # set()
