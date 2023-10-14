import calculator
a=None
while True:
    try:
        a=int(input("Enter your first number"))
        break
    except ValueError:
        print("invalid input, please enter a number")
b=None
while True:
    try:
        b=int(input("Enter your second number"))
        break
    except ValueError:
        print("invalid input, please enter a number")

result_add = calculator.add(a, b)
result_subtract = calculator.subtract(a, b)
result_multiply = calculator.multiply(a, b)
result_divide = calculator.divide(a, b)
print(f"Addition result: {result_add}")
print(f"Subtraction result: {result_subtract}")
print(f"Multiplication result: {result_multiply}")
print(f"Division result: {result_divide}")
