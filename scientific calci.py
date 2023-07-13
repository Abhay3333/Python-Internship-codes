import math


def scientific_calculator():
    print("Scientific Calculator")

    while True:
        print("\nSelect an operation:")
        print("1. Square root")
        print("2. Trigonometric functions")
        print("3. Logarithmic functions")
        print("4. Exponential function")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            number = float(input("Enter a number: "))
            result = math.sqrt(number)
            print("Square root of", number, "is", result)

        elif choice == '2':
            angle = float(input("Enter an angle in degrees: "))
            radians = math.radians(angle)
            print("Sin:", math.sin(radians))
            print("Cos:", math.cos(radians))
            print("Tan:", math.tan(radians))

        elif choice == '3':
            number = float(input("Enter a number: "))
            print("Log:", math.log10(number))
            print("Natural Log:", math.log(number))

        elif choice == '4':
            number = float(input("Enter a number: "))
            print("Exponential:", math.exp(number))

        elif choice == '5':
            print("Thank you for using the scientific calculator.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Run the scientific calculator
scientific_calculator()
