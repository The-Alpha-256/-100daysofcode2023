# Calculating the area of a rectangle:
length= None
while True:
    try:
        length= int(input("Please enter the length of your rectangle: "))
        break
    except ValueError:
        print("Invalid input, please enter a number.")
width= None
while True:
    try:
        width= int(input("Please enter the width of your rectangle: "))
        break
    except ValueError:
        print("Invalid input, please enter a number.")
def area(length, width):
    return length*width
Area=area(length,width)
print(f"The area of your rectangle is, {Area}")
