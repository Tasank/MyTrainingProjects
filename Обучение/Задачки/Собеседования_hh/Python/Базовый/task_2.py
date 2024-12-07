"""
Реализовать функцию ревёрса строки без использования срезов и методов
"""
# 1) входные данные - строка
# 2) алгоритм возращающий обратную строку
# 3) выходные данные - обратная строка
#
# то есть должен быть алгоритм который беря текущий символ из цикла вставляет его в начало строки


def palindrome(text):
    # 1 вариант(с циклом)
    for i in range(len(text) - 1, -1, -1):
        print(text[i], end='')

    print()

    # 2 вариант (с удалением элемента из конца списка)
    test_1 = list(text)
    data =''
    for _ in range(len(test_1)):
        data += test_1.pop()
    print(data)

    # 3 вариант (с добавлением элемента в начало списка)
    dat = []
    for value in text:
        dat.insert(0, value)
    print(''.join(dat))

    # 4 вариант(конкатенация)
    output = ''
    for value in text:
        output = value + output
    print(output)




palindrome('Тестовый текст')