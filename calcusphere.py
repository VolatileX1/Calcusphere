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

def log(num):
    return math.log(num)

def ln(num):
    return math.log(num, math.e)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

def percent(num, percentage):
    return (percentage/100) * num

def imperial_to_metric(inches):
    cm = inches * 2.54
    m = cm / 100
    return (cm, m)

def metric_to_imperial(cm):
    inches = cm / 2.54
    feet = int(inches // 12)
    remaining_inches = inches % 12
    return (inches, feet, remaining_inches)

def currency_conversion(amount, exchange_rate):
    return amount * exchange_rate

memory = []

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
print("10.Logarithm")
print("11.Natural Logarithm")
print("12.Factorial")
print("13.Percentage Calculation")
print("14.Imperial to Metric Conversion")
print("15.Metric to Imperial Conversion")
print("16.Currency Conversion")
print("17.Memory Function")

while True:
    choice = input("Enter choice(1-17): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        if choice != '6':
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            memory.append(str(num1) + "+" + str(num2) + "=" + str(add(num1, num2)))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            memory.append(str(num1) + "-" + str(num2) + "=" + str(subtract(num1, num2)))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            memory.append(str(num1) + "*" + str(num2) + "=" + str(multiply(num1, num2)))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            memory.append(str(num1) + "/" + str(num2) + "=" + str(divide(num1, num2)))
        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))
            memory.append(str(num1) + "^" + str(num2) + "=" + str(power(num1, num2)))
        elif choice == '6':
            print("sqrt(", num1, ")=", sqrt(num1))
            memory.append("sqrt(" + str(num1) + ")" + "=" + str(sqrt(num1)))
        else:
            print("Invalid Input")
    elif choice in ('7', '8', '9'):
        degrees = float(input("Enter degrees: "))

        if choice == '7':
            print("sin(", degrees, ")=", sin(degrees))
            memory.append("sin(" + str(degrees) + ")" + "=" + str(sin(degrees)))
        elif choice == '8':
            print("cos(", degrees, ")=", cos(degrees))
            memory.append("cos(" + str(degrees) + ")" + "=" + str(cos(degrees)))
        elif choice == '9':
            print("tan(", degrees, ")=", tan(degrees))
            memory.append("tan(" + str(degrees) + ")" + "=" + str(tan(degrees)))
        else:
            print("Invalid Input")
    elif choice == '10':
        num = float(input("Enter number: "))
        base = float(input("Enter base: "))
        print("log(", num, ",", base, ")=", log(num))
        memory.append("log(" + str(num) + "," + str(base) + ")" + "=" + str(log(num)))
    elif choice == '11':
        num = float(input("Enter number: "))
        print("ln(", num, ")=", ln(num))
        memory.append("ln(" + str(num) + ")" + "=" + str(ln(num)))
    elif choice == '12':
        num = int(input("Enter number: "))
        print(num, "!=", factorial(num))
        memory.append(str(num) + "!" + "=" + str(factorial(num)))
    elif choice == '13':
        num = float(input("Enter number: "))
        percentage = float(input("Enter percentage: "))
        print(percentage, "% of", num, "=", percent(num, percentage))
        memory.append(str(percentage) + "%" + "of" + str(num) + "=" + str(percent(num, percentage)))
    elif choice == '14':
        inches = float(input("Enter length in inches: "))
        cm, m = imperial_to_metric(inches)
        print(inches, "inches =", cm, "cm")
        print(inches, "inches =", m, "m")
        memory.append(str(inches) + "inches" + "=" + str(cm) + "cm")
        memory.append(str(inches) + "inches" + "=" + str(m) + "m")
    elif choice == '15':
        cm = float(input("Enter length in centimeters: "))
        inches, feet, remaining_inches = metric_to_imperial(cm)
        print(cm, "cm =", inches, "inches")
        print(cm, "cm =", feet, "feet and", remaining_inches, "inches")
        memory.append(str(cm) + "cm" + "=" + str(inches) + "inches")
        memory.append(str(cm) + "cm" + "=" + str(feet) + "feet" + str(remaining_inches) + "inches")
    elif choice == '16':
        amount = float(input("Enter amount: "))
        exchange_rate = float(input("Enter exchange rate: "))
        print(amount, "units =", currency_conversion(amount, exchange_rate), "units")
        memory.append(str(amount) + "units" + "=" + str(currency_conversion(amount, exchange_rate)) + "units")
    elif choice == '17':
        if not memory:
            print("Memory is empty!")
        else:
            print("Memory:")
            for i in range(len(memory)):
                print(i+1, ":", memory[i])
    else:
        print("Invalid Input") 
