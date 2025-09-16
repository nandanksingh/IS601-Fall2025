from app.calculator import Calculator

def main():
    calc = Calculator()

    print("Welcome to the Calculator App!")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter operation (e.g., add 5 3): ")

        if user_input.lower() == "exit":
            print("Exiting Calculator. Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input format. Example: add 5 3")
                continue

            operation, a, b = parts[0], float(parts[1]), float(parts[2])

            if operation == "add":
                result = calc.add(a, b)
            elif operation == "subtract":
                result = calc.subtract(a, b)
            elif operation == "multiply":
                result = calc.multiply(a, b)
            elif operation == "divide":
                result = calc.divide(a, b)
            else:
                print("Unknown operation. Try again.")
                continue

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

if __name__ == "__main__":
    main()
