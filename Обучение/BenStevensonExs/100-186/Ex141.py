"""
Упражнение 141. Английская пропись.
В данном упражнении вам необходимо написать функцию, принимающую в качестве входного параметра число от 0 до 999 и
 возвращающую строку прописью. Например, если значение параметра будет равно 142, функция должна вернуть следующую
 строку: «one hundred forty two». Используйте один или несколько словарей вместо условных конструкций if/elif/else
 для выработки решения этой задачи. Напишите основную программу, в которой пользователь будет вводить числовое
 значение, а на экран будет выводиться соответствующая сумма прописью.
"""
def nums_dict(number):
    ONES_DICT = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen'
    }
    TENS_DICT = {
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    if number < 20:
        return ONES_DICT[number]
    elif number < 100:
        # делим число отбросив остаток и умножаем на 10, чтобы получить число словаря TENS_DICT
        # возвращаем десятки если остаток равен 0, иначе прибавляем пробел и слово из {ONES_DICT}
        return TENS_DICT[number // 10 * 10] + ('' if number % 10 == 0 else ' ' + ONES_DICT[number % 10])
    else:
        # В конце добавляем значение ещё раз вызванной функции с числом делённым без остатка на 100
        return ONES_DICT[number // 100] + ' hundred' + ('' if number % 100 == 0 else ' ' + nums_dict(number % 100))

def main():
    try:
        number = int(input('Введите число от 1 до 999: '))
        if 0 > number > 999:
            print('Неправильно введено значение!')
        else:
            print(nums_dict(number))
    except ValueError:
        print('Ошибка!Неправильный ввод')
main()