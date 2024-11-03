"""
Необходимо реализовать функцию get_palindromes, которая на вход принимает список строк strings и
возвращает новый список, содержащий только строки-палиндромы из исходного списка.
"""
def get_palindromes(strings):
    return [i for i in strings if i == i[::-1]]
  # new_lst = []
  # for i in range(strings):
  #   if i == i[::-1]:
  #     new_lst.append(i)
  # return new_lst
