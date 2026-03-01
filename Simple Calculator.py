def add (a, b):
    return a + b

def subtract (a, b):

    return a - b
def multiply (a, b):

    return a * b
def divide(a, b):

    if b == 0:
        return "Error! Division by zero.\n"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error! Division by zero.\n"
    return a % b


def main():
    while True:
        print("SIMPLE CALCULATOR:")
        print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Modulo\n6. Exit")
    
        choice = input("Choose What you want to perform (1 - 6): ")    

        if choice == '6':
            print("Thanks! For using this calculator.")
            break

        if choice not in {'1', '2', '3', '4', '5'}:
            print("\nInvalid choice! Try again.\n")
            continue

        try:
            num1 = float(input("Enter a:"))
            num2 = float(input("Enter b:"))
        except ValueError:
            print("\nInvalid choice! Try again.\n")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            result = modulo(num1, num2)
        print("Result: ", result)   

if __name__ == "__main__":
    main()