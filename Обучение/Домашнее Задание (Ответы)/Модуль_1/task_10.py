"""
Напиши функцию, которая получает строку, разбивает её на слова и возвращает список из этих слов,
записанных задом наперёд.
"""

text = 'Мышка  украла сыр со стола'


def reverse_text_1(text):
    return text.split()[::-1]


# Решение без использования split()
def reverse_text_2(text):
    words = []
    word = ''

    for char in text:
        if char != ' ':
            word += char
        else:
            if word:
                words.append(word)
                word = ''
    # Добавляем последнее слова, если строка не заканчивается пробелом
    if word:
        words.append(word)
    return words[::-1]


print(reverse_text_1(text))
print(reverse_text_2(text))
