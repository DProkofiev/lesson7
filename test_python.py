import math

#Тесты встроенных функций

list_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def test_filter():
    list_digits_filtered = list(filter(lambda x: x % 2 == 0, list_digits))
    assert list_digits_filtered == [2, 4, 6, 8, 0]


def test_map():
    list_digits_mapped = list(map(lambda x: x + 1, list_digits))
    assert list_digits_mapped == [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]


def test_sorted():
    list_digits_sorted = sorted(list_digits)
    assert list_digits_sorted == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Тесты math- функций


def test_pi():
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert math.sqrt(4) == 2


def test_pow():
    assert math.pow(2, 2) == 4


def test_hypot():
    assert math.hypot(3.0, 4.0) == 5.0

