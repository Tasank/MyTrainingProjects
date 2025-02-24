
"""
Напиши функцию, которая будет складывать все значения из списка в одну строку. На вход функция будет принимать список, а возвращать строку.
"""

def sum_list(lst):
    text = ''
    for i in lst:
        text += str(i)
    return text
    # return ''.join(lst)

name = ['a', 'b', 'c', 'd', 'e']
print(sum_list(name))