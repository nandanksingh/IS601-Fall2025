# This file is called "operations.py". 
# It has four math functions: add, subtract, multiply, and divide.
# Think of them as tools to do basic math.

def addition(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtraction(a, b):
    """Subtract the second number from the first and return the result."""
    return a - b

def multiplication(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def division(a, b):
    """Divide the first number by the second and return the result."""
    if b == 0:
        # You can’t divide by zero, so we stop with an error.
        raise ValueError("Division by zero is not allowed.")
    return a / b
