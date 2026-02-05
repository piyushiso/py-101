# if
# Check if the value is set or not.
value = True
if value == True:
    print("Value is set.")
    
# if-else.
# Check if the redsignal is turned on or not, if true -> you can not pass, else you can.
redSignal = True
# if redSignal is True:
# if redSignal == True:
if redSignal:
    print("You can not pass.")
else:
    print("You can go now.")
    
# if-elif ladder.
# Check whether the color is red, green or yellow.
color = "Red"
# if color is "Red":
if color == "Red":
    print("Red Color.")
elif color == "Green":
    print("Green Color.")
else:
    print("Yellow Color.")
    
# and, or...
a = -10
b = 5
c = 55
if a > b and a > c:
    print(f"a ({a}) is the greatest among three numbers.")
elif b > a and b > c:
    print(f"b ({b}) is the greatest among three numbers.")
else:
    print(f"c ({c}) is the greatest among three numbers.")
    
# branced if-else
# Check if a number lies between 5 and 50, and is divisible by 2 or not.
a = 11
if 5 <= a and a <= 50:
    print("Falls in the range,", end=" ")
    if a % 2 == 0:
        print("and is divisible by 2.")
    else:
        print("and is not divisble by 2.")
else:
    print("Does not fall in the range.")
    
# if-else as ternary operator
# Input a string from the user, and set access variable according to the input.
name = str(input("Enter your name: "))
access = "admin" if name == "Piyush" else "normal user"
print(f"You have {access} access.")