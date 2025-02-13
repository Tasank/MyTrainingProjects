"""
Необходимо реализовать функцию get_common_elements,
которая на вход принимает два списка lst1 и lst2 чисел,
и возвращает новый список, содержащий только общие элементы,
которые встречаются и в первом, и во втором списке.
"""
lst1 = [4]
lst2 = [1, 2, 3]
def get_common_elements(lst1, lst2):
    new_lst = set(lst1) & set(lst2)
    return list(new_lst)

print(get_common_elements(lst1, lst2))
