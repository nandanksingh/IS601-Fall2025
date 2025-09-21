"""
This file is the "app/calculator/__init__.py" file. 
It contains a simple REPL calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

# First, we need to get some functions that can actually do the math for us. 
# These functions (addition, subtraction, multiplication, and division) are 
# in another file called "operations.py" in the "app" folder.
# This is like opening a toolbox and pulling out the tools we need to do our math.
from app.operations import addition, subtraction, multiplication, division


def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""

    # First, we print a message to welcome the user to the calculator.
    print("Welcome to the calculator REPL! Type 'exit' to quit")

    # This is the part where the calculator keeps running. 
    # The 'while True' means we are going to keep asking for input until the user quits.
    while True:
        # Now we ask the user to type something, like "add 5 3". 
        # This will get the operation (like "add") and two numbers from the user.
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")

        # This part checks if the user typed "exit". 
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break  # Stop the loop and exit the program.

        try:
            # Now we split the input into three parts: the operation and the two numbers.
            operation, num1, num2 = user_input.split()
            # Convert the numbers to floats so we can do math on them.
            num1, num2 = float(num1), float(num2)
        except ValueError:
            # If the user typed something wrong, show an error and restart the loop.
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue

        # Check what operation the user asked for and call the right function.
        if operation == "add":
            result = addition(num1, num2)
        elif operation == "subtract":
            result = subtraction(num1, num2)
        elif operation == "multiply":
            result = multiplication(num1, num2)
        elif operation == "divide":
            try:
                result = division(num1, num2)
            except ValueError as e:
                # Handle division by zero gracefully.
                print(e)
                continue
        else:
            # Unknown operation
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            continue

        # Print the result of the calculation.
        print(f"Result: {result}")


# Explanation of __init__.py:
# In Python, a file named "__init__.py" is really important. It tells Python that the folder it's in 
# (in this case, "calculator") is a special kind of folder called a "package". 
# Think of a package like a toolbox with different tools inside.
#
# Without the "__init__.py" file, Python won't know that the folder can be used to group code together. 
# It’s like a flag that says, "Hey Python, this folder can be used to import code!"
#
# For example, with this "__init__.py", we can import the calculator function by writing:
#   from app.calculator import calculator
