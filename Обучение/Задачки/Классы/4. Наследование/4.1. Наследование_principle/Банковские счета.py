"""
Создайте класс BankAccount с методами deposit(), withdraw() и check_balance().
Затем создайте классы CheckingAccount и SavingsAccount, которые наследуют свойства и методы класса BankAccount.
Добавьте специфичные методы для каждого класса, например, CheckingAccount может иметь метод write_check(),
а SavingsAccount - add_interest().
"""

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        print("Пополнение счета")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount:
            print("Снятие денег")
            self.__balance -= amount
            return self.__balance
        else:
            print("Недостаточно средств")

    def check_balance(self):
        return self.__balance

    @property
    def balance(self):
        return self.__balance

class CheckingAccount(BankAccount):
    def write_check(self, amount):
        if self.balance >= amount:
            print(f"Печатаем чек на сумму {amount}")
        else:
            print("Недостаточно средств для печати чека")

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if self.balance > 0:
            interest = self.balance * rate
            self.deposit(interest)
            print(f"Проценты добавлены: {interest}")
        else:
            print("Проценты не могут быть добавлены")

# Пример использования
my_bank = BankAccount()
my_bank.deposit(10)
my_bank.withdraw(5)
print(my_bank.check_balance())

my_checking = CheckingAccount()
my_checking.deposit(10)
my_checking.withdraw(5)
my_checking.write_check(5)

my_savings = SavingsAccount()
my_savings.deposit(10)
my_savings.withdraw(5)
my_savings.add_interest(0.05)
