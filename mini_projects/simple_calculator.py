num1 = int(input("Enter first number:" ))
num2 = int(input("Enter second number:"))

operation = input("Enter operation [+, -, *, /, **, %] :")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    
elif operation == "%":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")

elif operation == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
else:
    print("Invalid operation")


