"""
Упражнение 131. Инфиксная запись – в постфиксную.
Используйте свои наработки из упражнений 129 и 130 для разделения математических выражений на лексемы и поиска в них
унарных операторов. После этого используйте алгоритм, приведенный выше, для преобразования выражения из инфиксной формы
в постфиксную. Код, реализующий этот алгоритм, должен быть заключен в функцию, принимающую на вход список лексем
инфиксного выражения. Возвращать функция будет список лексем в постфиксном
выражении. В основной программе продемонстрируйте работу функции по преобразованию инфиксной формы записи
математического выражения в постфиксную. Запросите у пользователя выражение инфиксного типа и выведите на экран
его постфиксный аналог.
"""

# Сначала проверьте, удовлетворяет ли вас результат программы, прежде чем её копировать.
def isOperator(c):
    return not (c >= 'а' and c <= 'я') and not (c >= '0' and c <= '9') and not (c >= 'А' and c <= 'Я')


def getPriority(C):
    if C == '-' or C == '+':
        return 1
    elif C == '*' or C == '/':
        return 2
    elif C == '^':
        return 3
    return 0


def infixToPostfix(infix):
    operators = []
    operands = []

    for i in range(len(infix)):

        if infix[i] == '(':
            operators.append(infix[i])

        elif (infix[i] == ')'):
            while len(operators) != 0 and (operators[-1] != '('):
                op1 = operands[-1]
                operands.pop()
                op2 = operands[-1]
                operands.pop()
                op = operators[-1]
                operators.pop()
                tmp = op + op2 + op1
                operands.append(tmp)
            operators.pop()
        elif not isOperator(infix[i]):
            operands.append(infix[i] + "")

        else:
            while len(operators) != 0 and getPriority(infix[i]) <= getPriority(operators[-1]):
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()

                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])

    while len(operators) != 0:
        op1 = operands[-1]
        operands.pop()

        op2 = operands[-1]
        operands.pop()

        op = operators[-1]
        operators.pop()

        tmp = op + op2 + op1
        operands.append(tmp)
    return operands[-1]

def main():
    s = input("Введите инфиксное выражение: ")
    print("Постфиксный результат: ", infixToPostfix(s))

if __name__ == '__main__':
    main()