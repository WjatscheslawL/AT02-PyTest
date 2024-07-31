from main import check
from main import isPalindrome
from main import sortList

class TestMath(unittest_TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(3 - 2, 1)


if __name__ == "__main__":
    unittest.main()

def test_check():
    assert check(6) == True


def check2():
    assert check(3) == False


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (5, False),
    (0, True),
    (56, True),
    (-3, False)
])
def test_check_with_param(number, expected):
    assert check(number) == expected


def test_isPalindrome():
    assert isPalindrome('madam') == True
    assert isPalindrome('hello') == False


@pytest.mark.parametrize("test_input,expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])
def test_isPalindrome(test_input, expected):
    assert isPalindrome(test_input) == expected


def test_sort1():
    assert sortList([5, 6, 3, 1, 2]) == [1, 2, 3, 5, 6]


def test_sort2():
    assert sortList([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]
