"""
Задача: Анализ данных о продажах

У вас есть данные о продажах за месяц в файле CSV. Ваша задача — загрузить данные,
провести базовый анализ и получить несколько ключевых метрик.
"""

import pandas as pd

# Загрузка данных
df = pd.read_csv('sales_data.csv')

# Просмотр первых нескольких строк
print(df.head())

print('\nИнформация о DataFrame:')
print(df.info())

# Рассчитайте основные метрики
total_sales = df['amount'].sum()
average_sales = df['amount'].mean() # средняя сумма продаж
max_sales_day = df.loc[df['amount'].idxmax(), 'date']

print(f'\nОбщая сумма продаж: {total_sales}')
print(f'Средняя сумма продаж: {average_sales}')
print(f'День с максимальной продажей: {max_sales_day}')