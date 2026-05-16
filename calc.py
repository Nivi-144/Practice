import math

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Log (base 10)")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 11:
        print("Calculator Closed")
        break

    # For square root, log, sin, cos, tan
    if choice in [6, 7, 8, 9, 10]:
        num = float(input("Enter number: "))

        if choice == 6:
            print("Result =", math.sqrt(num))

        elif choice == 7:
            print("Result =", math.log10(num))

        elif choice == 8:
            print("Result =", math.sin(math.radians(num)))

        elif choice == 9:
            print("Result =", math.cos(math.radians(num)))

        elif choice == 10:
            print("Result =", math.tan(math.radians(num)))

    # For basic operations
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", num1 + num2)

        elif choice == 2:
            print("Result =", num1 - num2)

        elif choice == 3:
            print("Result =", num1 * num2)

        elif choice == 4:
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Division by zero not possible")

        elif choice == 5:
            print("Result =", math.pow(num1, num2))

        else:
            print("Invalid Choice")
