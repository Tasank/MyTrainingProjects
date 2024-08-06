# Рекурсивная функция должна проверять является ли строка палиндромом

def palindrome_check(line):
    if len(line) <= 1:
        return True
    return line[0] == line[-1] and palindrome_check(line[1:-1])

def main():
    s = input('Ввод строки: ')
    if palindrome_check(s):
        print('Это палиндром.')
    else:
        print('Это не палиндром.')

if __name__ == '__main__':
    main()