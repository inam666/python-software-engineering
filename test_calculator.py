import pytest
from calculator import add, divide, subtract, multiply


# --------------------
# Addition
# --------------------

def test_add():
    result = add(2, 3)
    assert result == 5


# --------------------
# Subtraction
# --------------------

def test_subtract():
    result = subtract(10, 3)
    assert result == 7


# --------------------
# Multiplication
# --------------------

def test_multiply():
    result = multiply(4, 5)
    assert result == 20


def test_multiply_by_zero():
    result = multiply(10, 0)
    assert result == 0


def test_multiply_negative():
    result = multiply(-4, 5)
    assert result == -20


def test_multiply_decimal():
    result = multiply(2.5, 4)
    assert result == 10.0


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (4, 5, 20),
    (10, 0, 0),
    (-4, 5, -20),
    (2.5, 4, 10.0),
])
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected


# --------------------
# Division
# --------------------

def test_divide():
    result = divide(10, 2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_negative():
    result = divide(-10, 2)
    assert result == -5


def test_divide_zero():
    result = divide(0, 5)
    assert result == 0


def test_divide_decimal():
    result = divide(7, 2)
    assert result == 3.5


def test_divide_by_one():
    result = divide(10, 1)
    assert result == 10