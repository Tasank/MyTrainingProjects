# Задача написать рекурсию реализующею суммирование чисел списка

def sum_list(data):

    if len(data) == 0:
        return 0
    else:
        return data[0] + sum_list(data[1:])


lst = [1, 2, 34, 23, 91, 3]
print(sum_list(lst))
