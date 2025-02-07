# Штрих-коды продуктов
product_1 = "101202245"
product_2 = "105202244"
product_3 = "912202333"
product_4 = "509202235"
product_5 = "001202309"

# Извлечение месяца и года
print(int(product_1[3:7]))

# month_1 = int(product_1[1:3])
# year_1 = int(product_1[3:7])

month_1, year_1 = int(product_1[1:3]), int(product_1[3:7])
month_2, year_2 = int(product_2[1:3]), int(product_2[3:7])
month_3, year_3 = int(product_3[1:3]), int(product_3[3:7])
month_4, year_4 = int(product_4[1:3]), int(product_4[3:7])
month_5, year_5 = int(product_5[1:3]), int(product_5[3:7])

# Сравнение дат
freshest_code = product_1
freshest_date = (year_1, month_1)

if (year_2, month_2) > freshest_date:
    freshest_code = product_2
    freshest_date = (year_2, month_2)

if (year_3, month_3) > freshest_date:
    freshest_code = product_3
    freshest_date = (year_3, month_3)

if (year_4, month_4) > freshest_date:
    freshest_code = product_4
    freshest_date = (year_4, month_4)

if (year_5, month_5) > freshest_date:
    freshest_code = product_5
    freshest_date = (year_5, month_5)

print(f"Самый свежий товар: {freshest_code}")
