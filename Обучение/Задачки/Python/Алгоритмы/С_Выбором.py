"""
Реализация алгоритма сортировки выбором
"""
def selection_sort(array):
    n = len(array)
    for i in range(n):
        # Находим минимальный элемент в оставшейся неотсортированной части массива
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        # Меняем найденный минимальный элемент с первым элементом неотсортированной части
        array[i], array[min_idx] = array[min_idx], array[i]
    return array