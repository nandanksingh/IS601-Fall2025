"""
main.py

Entry point for Assignment 3 - Command-Line Calculator (OOP version).
This script creates an instance of the Calculator class and starts the REPL interface.
"""

from app.calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
