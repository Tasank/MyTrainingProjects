from random import randint
combo_1 = ''
combo_2 = ''
count = 0


while combo_1 != 'PPP' and combo_2 != 'OOO':
    a = randint(0, 1)
    if a == 0:
        combo_1 += 'P'
        print('P', end=' ')
    elif a == 1:
        combo_2 += 'O'
        print('O', end=' ')
    count += 1

print(combo_1)
print(combo_2)
