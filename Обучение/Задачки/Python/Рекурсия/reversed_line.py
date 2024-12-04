# Функция должна рекурсивно вернуть строку в обратном порядке

def reversed_line(line):
    if len(line) <= 1:
        return line
    else:
        return line[-1] + reversed_line(line[0:-1])

s_input = input('Ввод строки: ')
print('Обратный порядок строки: ', reversed_line(s_input))
