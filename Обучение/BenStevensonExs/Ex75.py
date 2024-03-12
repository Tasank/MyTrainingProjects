"""
Упражнение 75. Палиндром или нет?
Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую,
является ли она палиндромом.
* Примечание программа подстроена по русский язык
"""
ask = input('Напишите своё слово: ')
reversed_ask = ''

print()
print("Проверка №1")
for i in range(len(ask), 0, -1):
    reversed_ask += ask[i - 1]
if ask == reversed_ask:
    print('Эта палиндром!')
else:
    print('Это не палиндром!')


# Второй способ
print()
print('Проверка №2')
reversed_ask_2 = ask[::-1]
if ask == reversed_ask_2:
    print('Эта палиндром!')
else:
    print('Это не палиндром!')

# Третий способ
print()
print("Проверка №3")
reversed_ask = "".join(reversed(ask))
if ask == reversed_ask:
    print('Эта палиндром!')
else:
    print('Это не палиндром!')



