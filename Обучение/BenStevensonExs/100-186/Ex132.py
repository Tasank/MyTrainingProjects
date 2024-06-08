"""
Упражнение 132. Выполнение постфиксных выражений.
Напишите программу, запрашивающую у пользователя математическое выражение в инфиксном виде, преобразующую его в
постфиксную форму, выполняющую полученное выражение и выводящую на экран результат.
Используйте при решении задачи свои наработки из упражнений 129, 130 и 131, а также алгоритм, приведенный выше(В книге)
"""
from Ex131 import infixToPostfix

def DecisionPostfix(postfix_tokens):
    values = []
    for tokens in postfix_tokens:
        if tokens in '+-*/':
            right = int(values.pop())
            left = int(values.pop())
            if tokens == '+': res = left + right
            elif tokens == '-': res = left - right
            elif tokens == '*': res = left * right
            else: res = left // right
            values.append(res)
        else:
            values.append(tokens)
    return values[0]
def main():
    expressions = input('Введите математическое выражение: ')
    # Постфиксный результат
    postfix = infixToPostfix(expressions)
    # вывод
    print(DecisionPostfix(postfix))
main()