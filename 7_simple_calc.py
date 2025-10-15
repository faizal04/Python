# Simple Calculator
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))
op = input("Enter a valid operator(+, -, * or /): ")

result = 0

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 + num2
elif op == "*":
    result = num1 * num1
elif op == "/":
    if num2 == 0:
        print("Error division by zero")
        exit()
    result = num1 / num2
else:
    print("Invalid operator")
    exit()

print(f"Result: {result}")
