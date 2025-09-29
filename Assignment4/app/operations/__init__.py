# This file is called "operations.py". 
# It has four math functions: add, subtract, multiply, and divide.
# Think of them as tools to do basic math.

# app/operation/__init__.py

class Operations:
    """A class that provides basic arithmetic operations."""

    @staticmethod
    def addition(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


