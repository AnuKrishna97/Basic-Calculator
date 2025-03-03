def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Undefined (division by zero)"

def calculator():
    while True:
        print("Welcome to Anu's Basic Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "5":
            print("Thank you for using Anu's Basic Calculator. Goodbye!")
            break
        
        if choice in ("1", "2", "3", "4"):
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                
                if choice == "1":
                    print("Result:", add(x, y))
                elif choice == "2":
                    print("Result:", subtract(x, y))
                elif choice == "3":
                    print("Result:", multiply(x, y))
                elif choice == "4":
                    print("Result:", divide(x, y))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Undefined input! Please enter a valid choice.")

if __name__ == "__main__":
    calculator()
