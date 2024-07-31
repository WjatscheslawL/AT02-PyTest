import pytest


def count_vowels(text: str) -> int:
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
