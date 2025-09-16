import pytest
from app.calculator import Calculator

calc = Calculator()

# Addition
def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, -1) == -2

# Subtraction
def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5

# Multiplication
def test_multiply():
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6

# Division
def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

