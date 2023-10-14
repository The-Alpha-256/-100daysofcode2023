Age = None
while True:
    try:
        Age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Invalid input, please enter a valid integer for the age.")
if Age >= 18:
    print("Your an Adult, therfore are eligible to Vote")
else:
    print("Your still young, but once you clock 18, you'll be able to vote")