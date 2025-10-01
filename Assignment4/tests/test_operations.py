# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 09/30/2025
# Project: Assignment 4 - Professional Calculator CLI
# ----------------------------------------------------------

"""tests/test_operations.py

Unit tests for the Operations class.
Covers addition, subtraction, multiplication, and division methods,
including positive, negative, float, and edge cases.
"""

import pytest
from app.operations import Operations


# ---------------------------
# Addition Tests
# ---------------------------
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (-2, -3, -5),
    (2.5, 3.5, 6.0),
])
def test_addition(a, b, expected):
    """Verify addition handles positive, negative, and float values."""
    result = Operations.addition(a, b)
    assert result == expected


# ---------------------------
# Subtraction Tests
# ---------------------------
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (10, 5, 5),
    (-5, -3, -2),
    (3, 5, -2),
])
def test_subtraction(a, b, expected):
    """Verify subtraction handles positive, negative, and mixed values."""
    result = Operations.subtraction(a, b)
    assert result == expected


# ---------------------------
# Multiplication Tests
# ---------------------------
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 10, 0),
    (0, 0, 0),         
    (-2, -3, 6),
    (2, -3, -6),
    (2.5, 4.0, 10.0),
])
def test_multiplication(a, b, expected):
    """Verify multiplication handles positive, negative, zero, and float values."""
    result = Operations.multiplication(a, b)
    assert result == expected


# ---------------------------
# Division Tests
# ---------------------------
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-6, -3, 2),
    (6, -3, -2),
    (2.5, 0.5, 5.0),
    (0, 5, 0.0),       
])
def test_division(a, b, expected):
    """Verify division handles positive, negative, zero numerator, and float values."""
    result = Operations.division(a, b)
    assert result == expected


def test_division_by_zero():
    """Ensure division by zero raises ValueError with clear message."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(1, 0)
