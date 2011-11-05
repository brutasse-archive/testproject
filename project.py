"""
A test project for CI testing.
"""

def add(a, b):
    return a + b

def multiply(a, b):
    return a + b


def test_add():
    assert add(1, 5) == 6
    assert add(12, 12) == 24
