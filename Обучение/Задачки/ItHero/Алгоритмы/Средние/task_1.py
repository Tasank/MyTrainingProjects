"""
Сконструировать валидные скобки
Вам дано число n - количество имеющихся пар скобок. Напишите функцию generateParenthesis,
которая будет возвращать список всех возможных валидных комбинаций скобок.

Примечание: Валидными называются скобки, которые закрываются скобками того же вида.
Пример 1:

generateParenthesis(3)

Результат: ["((()))","(()())","(())()","()(())","()()()"]

Пример 2:

generateParenthesis(1)

Результат: ["()"]
"""

def generateParenthesis(n):
    def backtrack(open_paren, close_paren, current_combination):
        """
        Рекурсивная функция для генерации всех валидных комбинаций скобок.
        :param open_paren: количество открытых скобок в текущей комбинации.
        :param close_paren: количество закрытых скобок в текущей комбинации.
        :param current_combination: текущая комбинация скобок.
        :return:
        """

        if len(current_combination) == 2 * n:
            result.append("".join(current_combination))
            return
        if open_paren < n:
            current_combination.append("(")
            backtrack(open_paren + 1, close_paren, current_combination)
            # Удаляем последнюю скобку, чтобы продолжить генерацию комбинаций с открытой скобой
            current_combination.pop()
        if close_paren < open_paren:
            current_combination.append(")")
            backtrack(open_paren, close_paren + 1, current_combination)
            current_combination.pop()

    result = []
    backtrack(0, 0, [])
    return result
print(generateParenthesis(3))