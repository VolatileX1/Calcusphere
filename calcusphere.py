import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def sqrt(num):
    return math.sqrt(num)

def sin(degrees):
    radians = math.radians(degrees)
    return math.sin(radians)

def cos(degrees):
    radians = math.radians(degrees)
    return math.cos(radians)

def tan(degrees):
    radians = math.radians(degrees)
    return math.tan(radians)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Sqrt")
print("7.Sine")
print("8.Cosine")
print("9.Tangent")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        if choice != '6':
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))
        elif choice == '6':
            print("sqrt(", num1, ")=", sqrt(num1))
        else:
            print("Invalid Input")
    elif choice in ('7', '8', '9'):
        degrees = float(input("Enter degrees: "))

        if choice == '7':
            print("sin(", degrees, ")=", sin(degrees))
        elif choice == '8':
            print("cos(", degrees, ")=", cos(degrees))
        elif choice == '9':
            print("tan(", degrees, ")=", tan(degrees))
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
