import pytest
import sqlite3


def test_add2():
    assert 1 + 1 == 2


def test_subtract():
    assert 3 - 2 == 1


def check(number):
    return number % 2 == 0


def isPalindrome(s):
    return s == s[::-1]


def sortList(numbers):
    return sorted(numbers)
