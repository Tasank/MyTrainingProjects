def sum_list(lst):
    text = ''
    for i in lst:
        text += i
    return text
    # return ''.join(lst)

name = ['a', 'b', 'c', 'd', 'e']
print(sum_list(name))