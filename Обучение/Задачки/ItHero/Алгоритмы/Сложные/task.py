"""
Разбивка по словам
Вам дана строка s и список words. Добавьте пробелы в s таким образом,
чтобы составить из исходной строки предложение, где каждое слово будет словом из списка words.
Напишите функцию wordBreak, которая вернет список всех возможных предложений.
Если из списка words нельзя составить строку s - верните пустой список.
"""
s = "catsanddog"
words = ["cat", "cats", "and", "sand", "dog"]


def wordBreak(s, words) -> list:
    def backtrack(start) -> list:
        if start == len(s):
            return [[]]  # Вернули пустой список, представляющий полное предложение

        if start in memo:
            return memo[start]

        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words_set:
                for sublist in backtrack(end):
                    result.append([word] + sublist)

        memo[start] = result
        return result

    words_set = set(words)
    memo = {}
    word_lists = backtrack(0)
    return [" ".join(words) for words in word_lists]


# Примеры использования
s1 = "catsanddog"
words1 = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s1, words1))  # ["cats and dog","cat sand dog"]

s2 = "pineapplepenapple"
words2 = ["apple", "pen", "applepen", "pine", "pineapple"]
print(wordBreak(s2, words2))  # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

s3 = "catsandog"
words3 = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s3, words3))  # []
