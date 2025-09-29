"""
main.py

This is the entry point for the Professional Calculator application.
It imports the calculator REPL and runs it when executed directly.

Usage:
    python main.py
"""

from app.calculator import calculator


def main():
    """Run the calculator REPL."""
    calculator()


if __name__ == "__main__":
    main()
