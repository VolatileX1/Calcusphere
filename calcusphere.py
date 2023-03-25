import math
import matplotlib.pyplot as plt

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

def arcsin(value):
    radians = math.asin(value)
    return math.degrees(radians)

def arccos(value):
    radians = math.acos(value)
    return math.degrees(radians)

def arctan(value):
    radians = math.atan(value)
    return math.degrees(radians)

def log(num, base):
    return math.log(num, base)

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
print("10.Arcsine")
print("11.Arccosine")
print("12.Arctangent")
print("13.Logarithm")
print("14.Natural Logarithm")
print("15.Factorial")
print("16.Percentage Calculation")
print("17.Imperial to Metric Conversion")
print("18.Metric to Imperial Conversion")
print("19.Currency Conversion")
print("20.Memory Function")
print("21.Graphing")

while True:
    choice = input("Enter choice(1-21): ")

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
    elif choice in ('7', '8', '9', '10', '11', '12'):
        degrees = float(input("Enter degrees: "))

        if choice == '7':
            print("sin(", degrees, ")=", sin(degrees))
            memory.append("sin(" + str(degrees) + ")=" + str(sin(degrees)))

        elif choice == '8':
            print("cos(", degrees, ")=", cos(degrees))
            memory.append("cos(" + str(degrees) + ")=" + str(cos(degrees)))
        elif choice == '9':
            print("tan(", degrees, ")=", tan(degrees))
            memory.append("tan(" + str(degrees) + ")=" + str(tan(degrees)))
        elif choice == '10':
            value = float(input("Enter the value of sin: "))
            print("arcsin(", value, ")=", arcsin(value))
            memory.append("arcsin(" + str(value) + ")=" + str(arcsin(value)))
        elif choice == '11':
            value = float(input("Enter the value of cos: "))
            print("arccos(", value, ")=", arccos(value))
            memory.append("arccos(" + str(value) + ")=" + str(arccos(value)))
        elif choice == '12':
            value = float(input("Enter the value of tan: "))
            print("arctan(", value, ")=", arctan(value))
            memory.append("arctan(" + str(value) + ")=" + str(arctan(value)))
        else:
            print("Invalid Input")
    elif choice in ('13', '14'):
        num = float(input("Enter a number: "))

        if choice == '13':
            base = int(input("Enter the base: "))
            print("log(", num, ",", base, ")=", log(num, base))
            memory.append("log(" + str(num) + "," + str(base) + ")=" + str(log(num, base)))
        elif choice == '14':
            print("ln(", num, ")=", ln(num))
            memory.append("ln(" + str(num) + ")=" + str(ln(num)))
        else:
            print("Invalid Input")
    elif choice == '15':
        num = int(input("Enter a number: "))
        print(num, "!=", factorial(num))
        memory.append(str(num) + "!=" + str(factorial(num)))
    elif choice == '16':
        num = float(input("Enter the number: "))
        percentage = float(input("Enter the percentage: "))
        print(percentage, "% of", num, "=", percent(num, percentage))
        memory.append(str(percentage) + "% of" + str(num) + "=" + str(percent(num, percentage)))
    elif choice == '17':
        inches = float(input("Enter the length in inches: "))
        cm, m = imperial_to_metric(inches)
        print(inches, "inches =", cm, "cm /", m, "meters")
        memory.append(str(inches) + "inches =" + str(cm) + "cm /" + str(m) + "meters")
    elif choice == '18':
        cm = float(input("Enter the length in centimeters: "))
        inches, feet, remaining_inches = metric_to_imperial(cm)
        print(cm, "cm =", inches, "inches /", feet, "feet and", remaining_inches, "inches")
        memory.append(str(cm) + "cm =" + str(inches) + "inches /" + str(feet) + "feet and" + str(remaining_inches) + "inches")
    elif choice == '19':
        amount = float(input("Enter the amount in USD: "))
        exchange_rate = float(input("Enter the exchange rate: "))
        print(amount, "USD =", currency_conversion(amount, exchange_rate), "foreign currency")
        memory.append(str(amount) + "USD =" + str(currency_conversion(amount, exchange_rate)) + "foreign currency")
    elif choice == '20':
        print("Memory:", memory)
    elif choice == '21':
        expr = input("Enter a mathematical expression: ")
        x_vals = []
        y_vals = []

        for i in range(-360, 361):
            x = i
            try:
                y = eval(expr)
            except ZeroDivisionError:
                y = float('inf')
            except:
                continue
            x_vals.append(x)
            y_vals.append(y)

        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of ' + expr)
        plt.show()
    else:
        print("Invalid Input")
