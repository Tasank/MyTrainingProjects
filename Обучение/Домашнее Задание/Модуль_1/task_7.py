num_list = [343, 35, 46, 464, 5, 234, 645, 64, 56, 35]
min_num = num_list[0]

for num in num_list:
    if num < min_num:
        min_num = num

print(min_num)