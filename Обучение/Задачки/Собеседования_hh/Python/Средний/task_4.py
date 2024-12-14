"""
Вы разрабатываете программу для проверки безопасности паролей.
Ваша задача — проверить список паролей и определить, какие из них безопасны.
Пароль считается таковым, если он удовлетворяет пяти условиям:

1) Содержит хотя бы одну заглавную букву;
2) Содержит хотя бы одну строчную букву;
3) Содержит хотя бы одну цифру;
4) Содержит хотя бы один специальный символ (допустимый набор символов: !@#$%^&*()-+);
5) Длина пароля больше или равна 8 символам.

Формат ввода
Одна строка, в которой чередуются пароли, разделенные пробелами. Длина строки — не более 100 символов.

Формат вывода
Одна строка, в которой содержатся только безопасные пароли, разделенные пробелами.
Выводите пароли в том порядке, в котором они были даны на вход.
Если подходящих паролей нет, выводите «Не найдено» (без кавычек).
Пример 1

Входные данные:
Password1 Pass@word 12345 pass!word Passw@rd Password1!
Выходные данные:
Password1!

Пример 2
Входные данные:
Password1 Pass@word 12345 pass!word
Выходные данные:
Не найдено
"""

special_symbols = "!@#$%^&*()-+"


class CheckPasswords:
    def __init__(self, passwords):
        self.passwords = passwords.split()

    def is_safe_password(self, password):
        if len(password) < 8:
            return False
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in special_symbols for char in password)
        return has_upper and has_lower and has_digit and has_special

    def solve(self):
        safe_passwords = [password for password in self.passwords if self.is_safe_password(password)]
        if safe_passwords:
            return " ".join(safe_passwords)
        else:
            return "Не найдено"


input_string = input()
checker = CheckPasswords(input_string)
print(checker.solve())
