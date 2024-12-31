"""
Реализация алгоритма сортировки пузырьком.
"""

some_array = [21, 5, 6, 3, 98, 12, 321]


def sort_bubble(some_array):
    n = len(some_array)
    for i in range(n):
        for v in range(0, n - i - 1):
            if some_array[v] > some_array[v + 1]:
                some_array[v], some_array[v + 1] = some_array[v + 1], some_array[v]
    return some_array


print(sort_bubble(some_array))
