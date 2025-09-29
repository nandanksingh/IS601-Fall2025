"""
tests/test_calculator.py

Unit tests for the interactive calculator REPL.
Covers:
- Valid operations (add, subtract, multiply, divide)
- Invalid inputs and error handling
- Special commands (help, history)
- Edge cases and graceful exits

Uses:
- monkeypatch to simulate user input
- capsys to capture console output
"""

import sys
import pytest
from io import StringIO
from app.calculator import calculator


# -------------------------------------------------------------------
# Helper Function: Simulate REPL Input and Capture Output
# -------------------------------------------------------------------
def run_calculator_with_input(monkeypatch, inputs):
    """
    Simulates user input and captures calculator REPL output.

    Args:
        monkeypatch: pytest fixture for overriding input()
        inputs (list[str]): sequence of commands to simulate

    Returns:
        str: captured console output
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))

    captured_output = StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output
    try:
        with pytest.raises(SystemExit):
            calculator()  # exits when "exit" command is given
    finally:
        sys.stdout = original_stdout
    return captured_output.getvalue()


# -------------------------------------------------------------------
# Positive Tests: Valid Operations
# -------------------------------------------------------------------

def test_addition(monkeypatch):
    inputs = ["add 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output


def test_subtraction(monkeypatch):
    inputs = ["subtract 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output


def test_multiplication(monkeypatch):
    inputs = ["multiply 4 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 20.0" in output


def test_division(monkeypatch):
    inputs = ["divide 10 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output


# -------------------------------------------------------------------
# Negative Tests: Invalid Inputs and Errors
# -------------------------------------------------------------------

def test_invalid_operation(monkeypatch):
    inputs = ["modulus 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unsupported calculation type" in output


def test_invalid_input_format(monkeypatch):
    inputs = ["add two three", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid format" in output


def test_division_by_zero(monkeypatch):
    inputs = ["divide 5 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed" in output


# -------------------------------------------------------------------
# Special Command Tests: Help and History
# -------------------------------------------------------------------

def test_help_command(monkeypatch):
    inputs = ["help", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Calculator REPL - Help" in output
    assert "Supported operations:" in output


def test_history_command(monkeypatch):
    inputs = ["add 2 2", "history", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Calculation History" in output
    assert "Result: 4.0" in output


def test_display_history_empty(monkeypatch):
    """Covers the 'No calculations yet.' branch in display_history."""
    inputs = ["history", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "No calculations yet." in output


# -------------------------------------------------------------------
# Coverage / Edge Case Tests
# -------------------------------------------------------------------

def test_empty_input(monkeypatch):
    """Ensure empty input  is executed properly."""
    inputs = ["", "add 1 1", "exit"]
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        calculator()


def test_generic_execution_error(monkeypatch):
    """Trigger a generic exception inside calculation.execute() """
    class FaultyCalculation:
        def execute(self):
            raise Exception("Execution failed")

    monkeypatch.setattr("app.calculation.CalculationFactory.create_calculation", lambda *_: FaultyCalculation())

    inputs = ["add 1 1", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "An error occurred during calculation: Execution failed" in output
    assert "Please try again." in output


def test_keyboard_interrupt(monkeypatch):
    """Simulate Ctrl+C interrupt."""
    def raise_keyboard_interrupt(_):
        raise KeyboardInterrupt
    monkeypatch.setattr("builtins.input", raise_keyboard_interrupt)

    with pytest.raises(SystemExit):
        calculator()


def test_eof_error(monkeypatch):
    """Simulate Ctrl+D EOF error."""
    def raise_eof(_):
        raise EOFError
    monkeypatch.setattr("builtins.input", raise_eof)

    with pytest.raises(SystemExit):
        calculator()


def test_outermost_generic_exception(monkeypatch, capsys):
    """Force a generic exception to trigger sys.exit(1)."""
    def raise_generic(_):
        raise Exception("Boom!")

    monkeypatch.setattr("builtins.input", raise_generic)

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Unexpected error: Boom!" in captured.out