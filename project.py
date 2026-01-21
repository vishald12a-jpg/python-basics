# -----------------------------
# MODULE 1: MINI CALCULATOR
# -----------------------------

def get_number(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please enter a valid integer.")

def add():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print("Result:", a + b)

def subtract():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print("Result:", a - b)

def multiply():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print("Result:", a * b)

def divide():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", a / b)

def factorial():
    n = get_number("Enter a number: ")
    if n < 0:
        print("Factorial not defined for negative numbers")
        return
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)

def even_odd():
    n = get_number("Enter a number: ")
    print("Even Number" if n % 2 == 0 else "Odd Number")

def calculator_menu():
    while True:
        print("\n--- MINI CALCULATOR ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Factorial")
        print("6. Even/Odd Checker")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            factorial()
        elif choice == "6":
            even_odd()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")

calculator_menu()
