# Assignment 4 – Professional Calculator Command-Line Application

## Overview

This project is a **professional calculator** built as a Python command-line tool. It demonstrates how to apply **object-oriented programming (OOP)**, clean design, comprehensive error handling, and automated testing in practice.

The calculator supports the four main arithmetic operations (add, subtract, multiply, divide) and follows two important coding styles:

* **LBYL (Look Before You Leap)** → check before acting
* **EAFP (Easier to Ask Forgiveness than Permission)** → try and handle errors gracefully

The codebase is modular, organized into three main packages:

* `calculator` → REPL interface
* `calculation` → logic for creating and managing calculations
* `operations` → individual operation classes

This structure makes the code easy to maintain, extend, and reuse.


## Setup Instructions

1. Open the project folder:   cd IS601-Fall2025/Assignment4

2. Create and activate a virtual environment: 
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:    pip install -r requirements.txt


## Usage

Run the calculator: python main.py

Once started, the calculator enters **REPL mode**. You can type commands such as:
add 5 3  
subtract 10 4  
multiply 7 6  
divide 20 5  

### Special Commands

* `help` → Show instructions and available operations
* `history` → Show all calculations in the current session
* `exit` → Quit the calculator


## Error Handling

The program includes strong error handling for:

* Invalid or missing input format
* Division by zero
* Unexpected exceptions (with friendly messages)

This ensures the calculator is user-friendly and resilient.

---

## Testing

Testing is done using **pytest** with both unit and parameterized tests.

Run all tests: pytest

Run tests with coverage: pytest --cov=app --cov-report=term-missing


Achieves **100% test coverage**, including edge cases.
GitHub Actions CI is configured to run tests automatically on every push and enforce coverage requirements.


## Reflection

Working on this project improved my ability to apply advanced OOP in real code. I practiced all four pillars of OOP:

* **Abstraction** – separating what operations do from how they are done
* **Encapsulation** – keeping logic within classes
* **Inheritance** – reusing code across calculation types
* **Polymorphism** – allowing consistent execution across different operations

Testing was the most challenging part — especially for user input, error handling, and exit conditions. I learned how to use **monkeypatching** to simulate input and exceptions, and **subprocess testing** to cover the `__main__` entry point. These techniques gave me a deeper appreciation of how testing ensures code quality in professional applications.

Overall, this project strengthened my skills in OOP design, testing, and error handling, while also teaching me how to deliver production-quality code with confidence.

---

