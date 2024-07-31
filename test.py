import pytest
from main import count_vowels


@pytest.mark.parametrize("input_text, expected", [
    ("Привет, как дела?", 5),
    ("Это тестовая строка.", 8),
    ("", 0),
    ("БыстрАя лисА прыгнула черЕз ленивого пса.", 15),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0),
    ("аЕёИОУыЭюЯ", 10),
])
def test_count_vowels(input_text, expected):
    # for i, (input_text, expected) in enumerate(test_cases):
    result = count_vowels(input_text)
    i = 0
    assert result == expected, f"Ошибка в тесте {i + 1}: ожидалось {expected}, получено {result}"
    print(f"Тест {i + 1} прошел успешно.")
