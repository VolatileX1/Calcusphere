import math
import cmath
import sympy
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

def integrate(expression, variable, limits):
    x = sympy.symbols(variable)
    f = sympy.sympify(expression)
    a, b = limits
    result = sympy.integrate(f, (x, a, b))
    return result.evalf()

def differentiate(expression, variable):
    x = sympy.symbols(variable)
    f = sympy.sympify(expression)
    result = sympy.diff(f, x)
    return result

def complex_add(num1, num2):
    return num1 + num2

def complex_subtract(num1, num2):
    return num1 - num2

def complex_multiply(num1, num2):
    return num1 * num2

def complex_divide(num1, num2):
    return num1 / num2

def complex_power(num1, num2):
    return num1 ** num2

def complex_sqrt(num):
    return cmath.sqrt(num)

def complex_log(num, base):
    return cmath.log(num, base)

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
print("21.Integration")
print("22.Differentiation")
print("23.Complex Number Addition")
print("24.Complex Number Subtraction")
print("25.Complex Number Multiplication")
print("26.Complex Number Division")
print("27.Complex Number Power")
print("28.Complex Number Sqrt")
print("29.Complex Number Logarithm")
print("30.Graphing")

while True:
    choice = input("Enter choice(1-19): ")

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
            memory.append("sqrt(" + str(num1) + ")=" + str(sqrt(num1)))
    elif choice in ('7', '8', '9', '10', '11', '12'):
        degrees = float(input("Enter angle in degrees: "))
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
            value = float(input("Enter value: "))
            print("arcsin(", value, ")=", arcsin(value))
            memory.append("arcsin(" + str(value) + ")=" + str(arcsin(value)))
        elif choice == '11':
            value = float(input("Enter value: "))
            print("arccos(", value, ")=", arccos(value))
            memory.append("arccos(" + str(value) + ")=" + str(arccos(value)))
        elif choice == '12':
            value = float(input("Enter value: "))
            print("arctan(", value, ")=", arctan(value))
            memory.append("arctan(" + str(value) + ")=" + str(arctan(value)))
    elif choice in ('13', '14'):
        num = float(input("Enter number: "))
        if choice == '13':
            base = float(input("Enter base: "))
            print("log_", base, "(", num, ")=", log(num, base))
            memory.append("log_" + str(base) + "(" + str(num) + ")=" + str(log(num, base)))
        elif choice == '14':
            print("ln(", num, ")=", ln(num))
            memory.append("ln(" + str(num) + ")=" + str(ln(num)))
    elif choice == '15':
        num = int(input("Enter number: "))
        print(num, "!=", factorial(num))
        memory.append(str(num) + "!=" + str(factorial(num)))
    elif choice == '16':
        num = float(input("Enter number: "))
        percentage = float(input("Enter percentage: "))
        print(percentage, "% of", num, "=", percent(num, percentage))
        memory.append(str(percentage) + "% of" + str(num) + "=" + str(percent(num, percentage)))
    elif choice == '17':
        inches = float(input("Enter length in inches: "))
        cm, m = imperial_to_metric(inches)
        print(inches, "inches =", cm, "cm or", m, "meters")
        memory.append(str(inches) + "inches =" + str(cm) + "cm or" + str(m) + "meters")
    elif choice == '18':
        cm = float(input("Enter length in cm: "))
        inches, feet, remaining_inches = metric_to_imperial(cm)
        print(cm, "cm =", feet, "ft", remaining_inches, "inches or", inches, "inches")
        memory.append(str(cm) + "cm =" + str(feet) + "ft" + str(remaining_inches) + "inches or" + str(inches) + "inches")
    elif choice == '19':
        amount_str = input("Enter amount in USD: ")
    # Remove any non-numeric characters from the input string
        amount_str = ''.join(filter(lambda x: x.isdigit() or x == '.', amount_str))
        amount = float(amount_str)
    
        exchange_rate_str = input("Enter exchange rate: ")
import math
import cmath
import sympy
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

def integrate(expression, variable, limits):
    x = sympy.symbols(variable)
    f = sympy.sympify(expression)
    a, b = limits
    result = sympy.integrate(f, (x, a, b))
    return result.evalf()

def differentiate(expression, variable):
    x = sympy.symbols(variable)
    f = sympy.sympify(expression)
    result = sympy.diff(f, x)
    return result

def complex_add(num1, num2):
    return num1 + num2

def complex_subtract(num1, num2):
    return num1 - num2

def complex_multiply(num1, num2):
    return num1 * num2

def complex_divide(num1, num2):
    return num1 / num2

def complex_power(num1, num2):
    return num1 ** num2

def complex_sqrt(num):
    return cmath.sqrt(num)

def complex_log(num, base):
    return cmath.log(num, base)

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
print("21.Integration")
print("22.Differentiation")
print("23.Complex Number Addition")
print("24.Complex Number Subtraction")
print("25.Complex Number Multiplication")
print("26.Complex Number Division")
print("27.Complex Number Power")
print("28.Complex Number Sqrt")
print("29.Complex Number Logarithm")
print("30.Graphing")

while True:
    choice = input("Enter choice(1-19): ")

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
            memory.append("sqrt(" + str(num1) + ")=" + str(sqrt(num1)))
    elif choice in ('7', '8', '9', '10', '11', '12'):
        degrees = float(input("Enter angle in degrees: "))
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
            value = float(input("Enter value: "))
            print("arcsin(", value, ")=", arcsin(value))
            memory.append("arcsin(" + str(value) + ")=" + str(arcsin(value)))
        elif choice == '11':
            value = float(input("Enter value: "))
            print("arccos(", value, ")=", arccos(value))
            memory.append("arccos(" + str(value) + ")=" + str(arccos(value)))
        elif choice == '12':
            value = float(input("Enter value: "))
            print("arctan(", value, ")=", arctan(value))
            memory.append("arctan(" + str(value) + ")=" + str(arctan(value)))
    elif choice in ('13', '14'):
        num = float(input("Enter number: "))
        if choice == '13':
            base = float(input("Enter base: "))
            print("log_", base, "(", num, ")=", log(num, base))
            memory.append("log_" + str(base) + "(" + str(num) + ")=" + str(log(num, base)))
        elif choice == '14':
            print("ln(", num, ")=", ln(num))
            memory.append("ln(" + str(num) + ")=" + str(ln(num)))
    elif choice == '15':
        num = int(input("Enter number: "))
        print(num, "!=", factorial(num))
        memory.append(str(num) + "!=" + str(factorial(num)))
    elif choice == '16':
        num = float(input("Enter number: "))
        percentage = float(input("Enter percentage: "))
        print(percentage, "% of", num, "=", percent(num, percentage))
        memory.append(str(percentage) + "% of" + str(num) + "=" + str(percent(num, percentage)))
    elif choice == '17':
        inches = float(input("Enter length in inches: "))
        cm, m = imperial_to_metric(inches)
        print(inches, "inches =", cm, "cm or", m, "meters")
        memory.append(str(inches) + "inches =" + str(cm) + "cm or" + str(m) + "meters")
    elif choice == '18':
        cm = float(input("Enter length in cm: "))
        inches, feet, remaining_inches = metric_to_imperial(cm)
        print(cm, "cm =", feet, "ft", remaining_inches, "inches or", inches, "inches")
        memory.append(str(cm) + "cm =" + str(feet) + "ft" + str(remaining_inches) + "inches or" + str(inches) + "inches")
    elif choice == '19':
        amount = float(input("Enter amount in USD: "))
        exchange_rate = float(input("Enter exchange rate: "))
        print(amount, "USD =", currency_conversion(amount, exchange_rate), "currency")
        memory.append(str(amount) + "USD =" + str(currency_conversion(amount, exchange_rate)) + "currency")
    elif choice == '20':
        amount = float(input("Enter amount in USD: "))
        exchange_rate = float(input("Enter exchange rate: "))
        print(amount, "USD is equal to", currency_conversion(amount, exchange_rate), "CAD")
        memory.append(str(amount) + " USD is equal to " + str(currency_conversion(amount, exchange_rate)) + " CAD")
    elif choice in ('21', '22'):
        expression = input("Enter expression: ")
        variable = input("Enter variable: ")
        limits = input("Enter limits as tuple (start, end): ")
    if choice == '21':
        print("Integral of", expression, "with respect to", variable, "from", limits[0], "to", limits[1], "=", integrate(expression, variable, limits))
        memory.append("Integral of " + expression + " with respect to " + variable + " from " + str(limits[0]) + " to " + str(limits[1]) + "=" + str(integrate(expression, variable, limits)))
    elif choice == '22':
        print("Derivative of", expression, "with respect to", variable, "=", differentiate(expression, variable))
        memory.append("Derivative of " + expression + " with respect to " + variable + "=" + str(differentiate(expression, variable)))

    elif choice in ('23', '24', '25', '26', '27', '28', '29'):
        num1 = complex(input("Enter first complex number in the form a+bj: "))
        num2 = complex(input("Enter second complex number in the form a+bj: "))

    if choice == '23':
        print(num1, "+", num2, "=", complex_add(num1, num2))
        memory.append(str(num1) + "+" + str(num2) + "=" + str(complex_add(num1, num2)))
    elif choice == '24':
        print(num1, "-", num2, "=", complex_subtract(num1, num2))
        memory.append(str(num1) + "-" + str(num2) + "=" + str(complex_subtract(num1, num2)))
    elif choice == '25':
        print(num1, "*", num2, "=", complex_multiply(num1, num2))
        memory.append(str(num1) + "*" + str(num2) + "=" + str(complex_multiply(num1, num2)))
    elif choice == '26':
        print(num1, "/", num2, "=", complex_divide(num1, num2))
        memory.append(str(num1) + "/" + str(num2) + "=" + str(complex_divide(num1, num2)))
    elif choice == '27':
        print(num1, "^", num2, "=", complex_power(num1, num2))
        memory.append(str(num1) + "^" + str(num2) + "=" + str(complex_power(num1, num2)))
    elif choice == '28':
        print("sqrt(", num1, ")=", complex_sqrt(num1))
        memory.append("sqrt(" + str(num1) + ")=" + str(complex_sqrt(num1)))
    elif choice == '29':
        base = float(input("Enter base: "))
        print("log_", base, "(", num1, ")=", complex_log(num1, base))
        memory.append("log_" + str(base) + "(" + str(num1) + ")=" + str(complex_log(num1, base)))
    elif choice == '30':
        expression = input("Enter expression in terms of x: ")
        x_list = []
        y_list = []
    for i in range(-10, 11):
        x = i
        y = eval(expression)
        x_list.append(x)
        y_list.append(y)
    plt.plot(x_list, y_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(expression)
    plt.show()

else:
    print("Invalid Input. Please Enter a number between 1 and 30.")

while True:
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() == 'no':
        break

print("Thank you for using the calculator!")
