

def sum(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

def rectangle_area(length, width):
    return length * width






def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Calculate triangle area")
        print("6. Calculate circle area")
        print("7. Calculate rectangle area")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")


        if choice == '1':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = sum(num1, num2)
            print("Sum:", result)
        elif choice == '2':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = sum(num1, num2)
            print("Subtraction:", result)
        elif choice == '3':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = subtract(num1, num2)
            print("Multiplication:", result)
        elif choice == '4':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = multiply(num1, num2)
            print("Division:", result)
        elif choice == '5':
            base = int(input("Enter the base of the triangle: "))
            height = int(input("Enter the height of the triangle: "))
            result = triangle_area(base, height)
            print("Triangle Area:", result)
        elif choice == '6':
            radius = int(input("Enter the radius of the circle: "))
            result = circle_area(radius)
            print("Circle Area:", result)
        elif choice == '7':
            length = int(input("Enter the length of the rectangle: "))
            width = int(input("Enter the width of the rectangle: "))
            result = rectangle_area(length, width)
            print("Rectangle Area:", result)
        elif choice == '8':
           exit()
           break
        else:
            print("Invalid choice. Please select a valid option (1-8).")

main_menu()