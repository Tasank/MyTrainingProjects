"""
Упражнение 176. Фонетический алфавит НАТО.
Напишите программу, которая будет запрашивать слово у пользователя и отображать его на экране
в виде шифра из соответствующих слов, обозначающих буквы исходного текста.
Например, если пользователь введет слово Hello, на экране должна быть отображена следующая последовательность слов:
Hotel Echo Lima Lima Oscar. Для решения этой задачи вам предстоит использовать рекурсивную функцию, а не циклы.
При этом все небуквенные символы, введенные пользователем, можно игнорировать.
"""
NATO_phonetic_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}


# Рекурсивная функция, возвращает слово, убирая и преобразовывая первый символ -> в алфавит НАТО
def NATO_chars(word):

    if not word:
        return ""
    first_char = word[0]
    if first_char in NATO_phonetic_alphabet:
        return NATO_phonetic_alphabet[first_char] + ' ' + NATO_chars(word[1:])
    else:
        return NATO_chars(word[1:])

word = input('Введите слово на английском: ').upper()
result = NATO_chars(word)
print(result)
