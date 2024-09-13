"""
Задание: Создайте класс BankAccount с calculated property balance,
которое вычисляет текущий баланс счета на основе списка транзакций.

Требования:

Класс BankAccount должен иметь метод add_transaction(amount), который добавляет новую транзакцию в список.
Calculated property balance должно вычислять сумму всех транзакций.
Создайте экземпляр класса BankAccount и добавьте несколько транзакций.
Выведите текущий баланс счета.
Подсказка: Используйте Python и создайте список транзакций в виде списка чисел.
Вычисление баланса можно реализовать с помощью метода sum().
"""
class BankAccount:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount):
        if type(amount) == int:
            print(f'Добавлена транзакция: {amount}')
            self.transactions.append(amount)
        else:
            raise ValueError("Требуется целое число")

    @property
    def balance(self):
        return sum(self.transactions)

my_bank = BankAccount()
my_bank.add_transaction(10)
my_bank.add_transaction(-1)
my_bank.add_transaction(300)
print(f'Текущий баланс: {my_bank.balance} рублей')
