"""
1) Чтение, добавление и изменение словарей.
2) Удаление пары ключ-значение.
3) Дополнительные операции со словарями.
4) Циклы и словари.
"""
print([1],end='\n\n')
# Создадим словарь с двумя парами ключ–значение
results = {"pass": 0, "fail": 0}

# Добавим третью пару ключ–значение
results["withdrawal"] = 1

# Обновим значения двух ключей в словаре
results["pass"] = 3
results["fail"] = results["fail"] + 1

# Выведем значения, ассоциированные с ключами fail, pass и withdrawal соответственно

print(results["fail"])
print(results["pass"])
print(results["withdrawal"])
print()
print('[2]',end='\n\n')

# Метод pop возвращает значение, ассоциированное с ключом удаленной пары из словаря.
print(results.pop('pass'))
print(results)
print()
print('[3]',end='\n\n')

# len
print('Текущее количество пар ключ-значение, присутствующих в словаре: ', len(results))

# in key
print('Входит ли в словарь ключ (fail) -> ', "fail" in results)
# in value
print('Входит ли в словарь значение (1) -> ', 1 in results.values())
print()

print('[4]',end='\n\n')
# Создаем словарь
constants = {"pi": 3.14, "e": 2.71, "root 2": 1.41}
# Выводим на экран все ключи и значения в отформатированном виде
for k in constants:
    print("Значение, ассоциированное с ключом", k, ": ", constants[k])

# Рассчитаем сумму значений в словаре
total = 0
for v in constants.values():
    total = total + v
# Выводим результат
print("Сумма значений составляет", total)

# Считаем, сколько раз пользователь ввел каждое значение
counts = {}
# Цикл, пока количество уникальных значений в словаре не достигнет пяти
while len(counts) < 5:
    s = input("Введите строку: ")
    # Если в словаре уже есть такой ключ, увеличиваем count на 1.
    # Иначе добавляем пару к словарю со значением count, равным 1.
    if s in counts:
        counts[s] = counts[s] + 1
    else:
        counts[s] = 1
# Выводим все строки и счетчики
for k in counts:
    print(k, "появилась в словаре", counts[k], "раз")

