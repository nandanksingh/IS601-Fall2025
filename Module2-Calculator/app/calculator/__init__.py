# Calculator with basic operations
class Calculator:

    # Addition
    def add(self, a, b):
        return a + b

    # Subtraction
    def subtract(self, a, b):
        return a - b

    # Multiplication
    def multiply(self, a, b):
        return a * b

    # Division
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b



# Explanation of __init__.py:
# In Python, a file named "__init__.py" is really important. It tells Python that the folder it's in (in this case, "calculator") 
# is a special kind of folder called a "package". Think of a package like a folder that contains related code, like a toolbox with
# different tools inside.
# 
# Without the "__init__.py" file, Python won't know that the folder can be used to group code together. It’s like a flag that says,
# "Hey Python, this folder can be used to import code!"
# 
# For example, if we put the "__init__.py" file in the "calculator" folder, we can import anything inside it by saying something like:
# "from app.calculator import calculator". The "__init__.py" file can be empty, or it can have code in it, but its main job is just 
# to make the folder a package.
