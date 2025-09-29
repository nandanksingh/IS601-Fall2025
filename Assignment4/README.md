
# Assignment 4 – Professional Calculator Command-Line Application

## Overview

This project implements a **professional-grade calculator** as a Python command-line application. It emphasizes clean architecture, object-oriented design, comprehensive error handling, and automated testing. The calculator supports basic arithmetic operations and demonstrates both **LBYL (Look Before You Leap)** and **EAFP (Easier to Ask Forgiveness than Permission)** programming paradigms.

The code follows modular design principles, separating concerns across packages (`calculator`, `calculation`, `operations`) to ensure maintainability and reusability.


## Setup Instructions

1. **Repository**

   cd IS601-Fall2025/Assignment4

2. **Create and Activate a Virtual Environment**

   python3 -m venv venv
   source venv/bin/activate   

3. **Install Dependencies**

   pip install -r requirements.txt


## Usage Instructions

To run the calculator from the terminal:  python main.py

Once started, the calculator enters a **REPL mode** (Read-Eval-Print Loop). You can type commands such as:

add 5 3
subtract 10 4
multiply 7 6
divide 20 5

### Special Commands

* `help` → Displays instructions and supported operations
* `history` → Shows all calculations from the session
* `exit` → Exits the calculator


## Testing

This project uses **pytest** with coverage to ensure correctness.

Run all tests:  pytest


Run tests with coverage report:

pytest --cov=app --cov-report=term-missing


The goal is **100% coverage**, enforced through GitHub Actions CI.


## Reflection

Building this project helped me strengthen my understanding of **object-oriented programming** and the **four pillars**:

* **Abstraction** – separating what operations do from how they are implemented.
* **Encapsulation** – keeping calculation details within well-defined classes.
* **Inheritance** – reusing structure across different calculation types.
* **Polymorphism** – allowing all calculations to be executed consistently through a shared interface.

Through this assignment, I also learned the importance of **error handling** in professional applications and how automated testing ensures confidence in code quality. Overall, this project connects academic learning with real-world practices in software development.


