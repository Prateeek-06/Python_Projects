import math

def calculator():
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log (base 10)")
    print("11. Natural Log (ln)")
    print("12. Factorial")
    print("0. Exit")
    while True:
        choice = input("Enter choice: ")

        if choice == "0":
            print("Calculator closed")
            break

        elif choice in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                print("Result:", a / b if b != 0 else "Error: divide by zero")
            elif choice == "5":
                print("Result:", math.pow(a, b))

        elif choice == "6":
            x = float(input("Enter number: "))
            print("Result:", math.sqrt(x))

        elif choice == "7":
            x = float(input("Enter angle in degrees: "))
            print("Result:", math.sin(math.radians(x)))

        elif choice == "8":
            x = float(input("Enter angle in degrees: "))
            print("Result:", math.cos(math.radians(x)))

        elif choice == "9":
            x = float(input("Enter angle in degrees: "))
            print("Result:", math.tan(math.radians(x)))

        elif choice == "10":
            x = float(input("Enter number: "))
            print("Result:", math.log10(x))

        elif choice == "11":
            x = float(input("Enter number: "))
            print("Result:", math.log(x))

        elif choice == "12":
            x = int(input("Enter number: "))
            print("Result:", math.factorial(x))

        else:
            print("Invalid choice")

calculator()
