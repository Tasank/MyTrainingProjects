"""
1) Чтение, добавление и изменение словарей.
2) Удаление пары ключ-значение.
3) Дополнительные операции со словарями.
"""
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

# Метод pop возвращает значение, ассоциированное с ключом удаленной пары из словаря.
print(results.pop('pass'))
print(results)
print()

# len
print('Текущее количество пар ключ-значение, присутствующих в словаре: ', len(results))

# in key
print('Входит ли в словарь ключ (fail) -> ', "fail" in results)
# in value
print('Входит ли в словарь значение (1) -> ', 1 in results.values())