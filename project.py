"""
A test project for CI testing.
"""

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / float(b)


def test_add():
    assert add(1, 5) == 6
    assert add(12, 12) == 24


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5


def test_division():
    assert divide(4, 2) == 2
    assert divide(6, 4) == 1.5
