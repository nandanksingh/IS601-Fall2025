"""
Calculation module for the Professional Calculator.

This module defines:
1. An abstract Calculation class (blueprint for all operations).
2. A CalculationFactory (responsible for creating calculation objects).
3. Concrete calculation classes (Add, Subtract, Multiply, Divide).

Key OOP Concepts Demonstrated:
- Abstraction: Using an abstract base class to define a contract.
- Encapsulation: Each calculation keeps its own numbers (`a`, `b`).
- Inheritance: All operations inherit from the Calculation base class.
- Polymorphism: All operations share the same interface (`execute`) but behave differently.
"""

from abc import ABC, abstractmethod
from app.operations import Operations


# -------------------------------
# Abstract Base Class: Calculation
# -------------------------------
class Calculation(ABC):
    """Blueprint for all calculations (add, subtract, multiply, divide)."""

    def __init__(self, a: float, b: float) -> None:
        """
        Initialize with two numbers.

        Args:
            a (float): First number
            b (float): Second number
        """
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:
        """
        Each subclass must implement its own version of this method.

        Returns:
            float: result of the calculation
        """
        pass  # pragma: no cover  # abstract method intentionally not executed

    def __str__(self) -> str:
        """Return a user-friendly string of the calculation result."""
        result = self.execute()
        operation_name = self.__class__.__name__.replace("Calculation", "")
        return f"{self.a} {operation_name} {self.b} = {result}"

    def __repr__(self) -> str:
        """Return a technical string for debugging."""
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


# -------------------------------
# Factory Class: CalculationFactory
# -------------------------------
class CalculationFactory:
    """Factory to create Calculation objects dynamically."""

    _calculations = {}

    @classmethod
    def register_calculation(cls, calc_type: str):
        """Decorator to register calculation classes in the factory."""

        def decorator(subclass):
            if calc_type.lower() in cls._calculations:
                raise ValueError(f"Calculation type '{calc_type}' is already registered.")
            cls._calculations[calc_type.lower()] = subclass
            return subclass

        return decorator

    @classmethod
    def create_calculation(cls, calc_type: str, a: float, b: float) -> "Calculation":
        """Create and return a Calculation object based on type."""
        calc_class = cls._calculations.get(calc_type.lower())
        if not calc_class:
            raise ValueError(
                f"Unsupported calculation type: '{calc_type}'. "
                f"Available: {', '.join(cls._calculations.keys())}"
            )
        return calc_class(a, b)


# -------------------------------
# Concrete Calculation Classes
# -------------------------------
@CalculationFactory.register_calculation("add")
class AddCalculation(Calculation):
    """Performs addition of two numbers."""

    def execute(self) -> float:
        return Operations.addition(self.a, self.b)


@CalculationFactory.register_calculation("subtract")
class SubtractCalculation(Calculation):
    """Performs subtraction of two numbers."""

    def execute(self) -> float:
        return Operations.subtraction(self.a, self.b)


@CalculationFactory.register_calculation("multiply")
class MultiplyCalculation(Calculation):
    """Performs multiplication of two numbers."""

    def execute(self) -> float:
        return Operations.multiplication(self.a, self.b)


@CalculationFactory.register_calculation("divide")
class DivideCalculation(Calculation):
    """Performs division of two numbers (with divide-by-zero check)."""

    def execute(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Operations.division(self.a, self.b)
