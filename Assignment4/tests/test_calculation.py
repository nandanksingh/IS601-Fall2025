# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 09/30/2025
# Project: Assignment 4 - Professional Calculator CLI
# ----------------------------------------------------------

"""
Advanced unit tests for Calculation classes and CalculationFactory.

- Uses unittest.mock.patch to isolate dependencies on Operations.
- Covers positive and negative scenarios for all operations.
- Ensures factory behavior, duplicate registration handling, and
  string/repr formatting are correct.
- Includes parameterized tests for efficiency.
- Exercises abstract base class behavior for full coverage.
"""

import pytest
from unittest.mock import patch
from app.operations import Operations
from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    Calculation,
)


# -------------------------------------------------------------------
# Tests for individual calculation classes
# -------------------------------------------------------------------

@patch.object(Operations, "addition", return_value=15)
def test_add_calculation_execute_positive(mock_add):
    calc = AddCalculation(10, 5)
    result = calc.execute()
    mock_add.assert_called_once_with(10, 5)
    assert result == 15


@patch.object(Operations, "addition", side_effect=Exception("Addition error"))
def test_add_calculation_execute_negative(mock_add):
    calc = AddCalculation(10, 5)
    with pytest.raises(Exception) as exc_info:
        calc.execute()
    assert str(exc_info.value) == "Addition error"


@patch.object(Operations, "subtraction", return_value=5)
def test_subtract_calculation_execute_positive(mock_sub):
    calc = SubtractCalculation(10, 5)
    result = calc.execute()
    mock_sub.assert_called_once_with(10, 5)
    assert result == 5


@patch.object(Operations, "multiplication", return_value=50)
def test_multiply_calculation_execute_positive(mock_mul):
    calc = MultiplyCalculation(10, 5)
    result = calc.execute()
    mock_mul.assert_called_once_with(10, 5)
    assert result == 50


@patch.object(Operations, "division", return_value=2)
def test_divide_calculation_execute_positive(mock_div):
    calc = DivideCalculation(10, 5)
    result = calc.execute()
    mock_div.assert_called_once_with(10, 5)
    assert result == 2


def test_divide_calculation_divide_by_zero():
    calc = DivideCalculation(10, 0)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        calc.execute()


# -------------------------------------------------------------------
# Tests for CalculationFactory
# -------------------------------------------------------------------

def test_factory_creates_add_calculation():
    calc = CalculationFactory.create_calculation("add", 2, 3)
    assert isinstance(calc, AddCalculation)
    assert calc.a == 2 and calc.b == 3


def test_factory_unsupported_type_lists_available():
    # ensure error message includes available keys
    with pytest.raises(ValueError) as exc:
        CalculationFactory.create_calculation("modulus", 2, 3)
    msg = str(exc.value)
    assert "Unsupported calculation type" in msg
    assert "add" in msg and "subtract" in msg and "multiply" in msg and "divide" in msg


def test_factory_register_duplicate():
    with pytest.raises(ValueError, match="already registered"):
        @CalculationFactory.register_calculation("add")
        class AnotherAdd(Calculation):
            def execute(self):
                return Operations.addition(self.a, self.b)


# -------------------------------------------------------------------
# Tests for string and repr
# -------------------------------------------------------------------

@patch.object(Operations, "addition", return_value=15)
def test_str_representation_add(mock_add):
    calc = AddCalculation(10, 5)
    result = str(calc)
    assert result == "10 Add 5 = 15"


def test_repr_representation_subtract():
    calc = SubtractCalculation(10, 5)
    assert repr(calc) == "SubtractCalculation(a=10, b=5)"


# -------------------------------------------------------------------
# Abstract class behavior
# -------------------------------------------------------------------

def test_calculation_abstract_cannot_instantiate():
    """Ensure Calculation cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Calculation(1, 2)  # abstract execute() not implemented


# -------------------------------------------------------------------
# Parameterized test
# -------------------------------------------------------------------

@pytest.mark.parametrize("calc_type, a, b, expected", [
    ("add", 10, 5, 15),
    ("subtract", 10, 5, 5),
    ("multiply", 10, 5, 50),
    ("divide", 20, 5, 4),
])
def test_parameterized_execute(calc_type, a, b, expected):
    calc = CalculationFactory.create_calculation(calc_type, a, b)
    result = calc.execute()
    assert result == expected
