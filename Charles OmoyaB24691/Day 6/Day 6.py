Name = input("Please enter your name: ")
Age = None
while True:
    try:
        Age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input, please enter a valid integer for the age.")

Number = None
while True:
    try:
        Number = float(input("Please enter a floating point number: "))
        break
    except ValueError:
        print("Invalid input, please enter a valid floating-point number.")

print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"Floating-Point number: {Number}")