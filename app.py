# app.py
from calculator import Calculator

def main():
    """
    Main function to run the scientific calculator application.
    """
    calc = Calculator()

    while True:
        print("\n--- Scientific Calculator ---")
        print("1: Square Root (√x)")
        print("2: Factorial (!x)")
        print("3: Natural Logarithm (ln(x))")
        print("4: Power (x^b)")
        print("5: Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                x = float(input("Enter a number: "))
                print(f"Result: {calc.square_root(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                x = int(input("Enter a non-negative integer: "))
                print(f"Result: {calc.factorial(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                x = float(input("Enter a positive number: "))
                print(f"Result: {calc.natural_log(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                x = float(input("Enter the base (x): "))
                b = float(input("Enter the exponent (b): "))
                print(f"Result: {calc.power(x, b)}")
            except ValueError:
                print("Error: Invalid input. Please enter numbers.")

        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()