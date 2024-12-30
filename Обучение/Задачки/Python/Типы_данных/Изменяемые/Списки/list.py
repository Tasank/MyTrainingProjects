"""
Дан произвольный список. Представьте его в обратном порядке.
"""

our_list = ['1', 2, 3]

# 1 вариант (реверс)
one_list = list(reversed(our_list))
# our_list.reverse()
print(one_list, end='\n\n')

# 2 вариант (срез)
two_list = our_list[::-1]
print(two_list, end='\n\n')

# 3 вариант (цикл)
three_list = []
for i in range(len(our_list)-1, -1, -1):
    three_list.append(our_list[i])
print(three_list, end='\n\n')

# 4 вариант
four_list = []
for el in our_list:
    four_list = [el] + four_list
print(four_list, end='\n\n')
