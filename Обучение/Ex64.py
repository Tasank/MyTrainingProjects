# Упражнение 64 Таблица со скидками
# Вывести таблицу: 1) с исходными ценами 2) Скидками 3)Новой ценой
# Для удобства покупателей


one_price = 4.95
two_price = 9.95
tree_price = 14.95
four_price = 19.95
five_price = 24.95
discount = 0.4

print('Исходная цена покупок: |%.2f$ | %.2f$ | %.2f$ | %.2f$ | %.2f$|' %(one_price, two_price,tree_price,four_price,five_price))
print('Скидки до 60 процентов:| 20%  |  30%  |  40%   |  50%   |   60% |')

one_price *= 0.8
two_price *= 0.7
tree_price *= 0.6
four_price *= 0.5
five_price *= 0.4

print('Новая цена:            |%.2f$ | %.2f$ | %.2f$  | %.2f$  | %.2f$ |' %(one_price, two_price,tree_price,four_price,five_price))



