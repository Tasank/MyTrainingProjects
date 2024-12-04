def check(n, t, a, b):
    # Проверяем, хватит ли T наборов для всех друзей
    total_ = sum(a)
    if total_ > t:
        return 'NO'  # Не хватит наборов для всех

    # Проверяем, что у каждого друга количество наборов лежит в диапазоне ai <= bi
    for i in range(n):
        if a[i] > b[i]:
            return 'NO'  # У друга i количество наборов выходит за пределы диапазона

    return 'YES'  # Все условия выполняются

# Считываем входные данные
n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Проверяем условия и выводим результат
result = check(n, t, a, b)
print(result)