import pytest

text_1 = 'DadaD'
text_2 = 'Noo'


def revered_text(text):
    data = ''
    for word in text.split():
        for letter in word:
            data = letter + data
    return data

def is_palindrome(text):
    if revered_text(text) == text:
        return 'Это палиндром'
    else:
        return 'Это не палиндром'

def test_is_palindrome():
    assert is_palindrome(text_1) == 'Это палиндром'
def test_is_not_palindrome():
    assert is_palindrome(text_2) == 'Это не палиндром'
