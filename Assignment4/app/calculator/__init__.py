"""
Professional Calculator REPL (Read-Eval-Print Loop)

Features:
- Perform arithmetic operations: add, subtract, multiply, divide
- Input validation and graceful error handling
- History tracking for calculations
- Helpful commands: help, history, exit
- Demonstrates LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission)
"""

# -------------------------------------------------------------------
# Imports and Setup
# -------------------------------------------------------------------
import sys
import readline  # Enables arrow-key navigation and history for user input
from typing import List
from app.calculation import Calculation, CalculationFactory


# -------------------------------------------------------------------
# Help Display Function
# -------------------------------------------------------------------
def display_help() -> None:
    """Show instructions and available commands."""
    help_message = """
Calculator REPL - Help
----------------------
Usage: <operation> <num1> <num2>

Supported operations:
    add       → Adds two numbers
    subtract  → Subtracts second number from first
    multiply  → Multiplies two numbers
    divide    → Divides first number by second

Special commands:
    help      → Show this message
    history   → Show past calculations
    exit      → Quit the calculator

Examples:
    add 10 5
    subtract 20 7
    multiply 6 9
    divide 15 3
"""
    print(help_message)


# -------------------------------------------------------------------
# History Display Function
# -------------------------------------------------------------------
def display_history(history: List[Calculation]) -> None:
    """Display past calculations stored in history."""
    if not history:  # LBYL: check before accessing
        print("No calculations yet.")
    else:
        print("Calculation History:")
        for i, calc in enumerate(history, start=1):
            print(f"{i}. {calc}")


# -------------------------------------------------------------------
# Main REPL Loop
# -------------------------------------------------------------------
def calculator() -> None:
    """
    Run the main calculator REPL loop.
    Handles commands, calculations, and errors gracefully.
    """
    history: List[Calculation] = []  # Store past calculations

    print("Welcome to the Professional Calculator REPL!")
    print("Type 'help' for usage or 'exit' to quit.\n")

    while True:
        try:
            # -------------------------------------------------------------------
            # User Input Handling
            # -------------------------------------------------------------------
            user_input: str = input(">> ").strip()

            if not user_input:  # LBYL: skip empty input
                continue

            # -------------------------------------------------------------------
            # Special Commands
            # -------------------------------------------------------------------
            command = user_input.lower()
            if command == "help":
                display_help()
                continue
            elif command == "history":
                display_history(history)
                continue
            elif command == "exit":
                print("Exiting calculator. Goodbye!")
                sys.exit(0)  # pragma: no cover

            # -------------------------------------------------------------------
            # Parse and Validate Input
            # -------------------------------------------------------------------
            try:
                operation, num1_str, num2_str = user_input.split()
                num1, num2 = float(num1_str), float(num2_str)
            except ValueError:
                print("Invalid format. Use: <operation> <num1> <num2>")
                continue

            # -------------------------------------------------------------------
            # Create Calculation Object
            # -------------------------------------------------------------------
            try:
                calculation = CalculationFactory.create_calculation(operation, num1, num2)
            except ValueError as e:
                print(e)
                continue

            # -------------------------------------------------------------------
            # Execute Calculation
            # -------------------------------------------------------------------
            try:
                result = calculation.execute()
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                continue
            except Exception as e:
                print(f"An error occurred during calculation: {e}")
                print("Please try again.\n")
                continue

            # -------------------------------------------------------------------
            # Display Result and Store History
            # -------------------------------------------------------------------
            print(f"Result: {result}\n")
            history.append(calculation)

        # -------------------------------------------------------------------
        # Graceful Exit Handling
        # -------------------------------------------------------------------
        except KeyboardInterrupt:  # Ctrl+C
            print("\nKeyboard interrupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)  # pragma: no cover
        except EOFError:  # Ctrl+D
            print("\nEOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)  # pragma: no cover
        except Exception as e:  # Final fallback
            print(f"\nUnexpected error: {e}")
            sys.exit(1)  # pragma: no cover


# -------------------------------------------------------------------
# Entry Point
# -------------------------------------------------------------------
if __name__ == "__main__":  # pragma: no cover
    calculator()