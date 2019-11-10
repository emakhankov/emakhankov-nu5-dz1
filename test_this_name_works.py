"""
Тесты встроенных функций
"""
import math

def test_filter():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    arr_f = list(filter(lambda x: x % 2 == 0, arr))
    assert arr_f == [2, 4, 6, 8, 0]


def test_map():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    arr_f = list(map(lambda x: x + 1, arr))
    assert arr_f == [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]


def test_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    arr_f = sorted(arr)
    assert arr_f == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_pi():
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert math.sqrt(4) == 2


def test_pow():
    assert math.pow(2,2) == 4


def test_hypot():
    assert math.hypot(3.0,4.0) == 5.0