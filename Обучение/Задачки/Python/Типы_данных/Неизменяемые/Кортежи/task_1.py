"""
Код создаёт список кортежей, где каждый кортеж содержит индекс и символ из строки word
"""

word = 'PyThoN ExAmPlE'
result = [(i, char) for i, char in enumerate(word) if char.islower()]
print(result)
print(type(result))
print(type(result[0]))

# перевести в кортеж
result = tuple(result)
print(result)
print(type(result))
# Они отличаются от списков в том, что кортежи не изменяемые
