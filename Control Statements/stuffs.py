# Conditions
# if statement only
# a = True
# if a is True:
#     print("A is True.")

# if else
# number = 301
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# if-elif ladder
# num = -0
# if num == 0:
#     print("Zero")
# elif num > 0:
#     print("Positive")
# else:
#     print("Negative")

# &&, || => and, or
# a = 100
# b = 15
# c = 500

# if a > b and a > c:
#     print(f"A ({a}) is the greatest among three numbers.")
# elif b > a and b > c:
#     print(f"B ({b}) is the greatest among three numbers.")
# else:
#     print(f"C ({c}) is the greatest among three numbers.")

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Can vote.")
# else:
#     print("Can not vote.")

# RGB -> PRIMARY / NON PRIMARY + RED -> R, GREEN -> G, BLUE -> B
# color = "Blue"
# if color == "Red" or color == "Blue" or color == "Green":
#     print("Primary Color, Code: ", end = " ")
#     if color == "Red": 
#         print("R")
#     elif color == "Green":
#         print("G")
#     else:
#         print("B")
# else:
#     print("Not a primary color.")

# Match Case...

# status_code = 200
# match status_code:
#     case 200:
#         print("Status Okay!")
#     case 404:
#         print("Not Found.")
#     case _:
#         print("Invalid.")

# number = 2
# option = 33

# match option:
#     case 1:
#         print(number ** 2)
#     case 2:
#         print(number ** 3)
#     case _:
#         print("Invalid")

# TERNARY
# age = 18
# can_vote = False
# if age > 17:
#     can_vote = True
# else:
#     can_vote = False
# print(can_vote)

# age = 17
# can_vote = "You can vote" if age > 17 else "You can not vote"
# print(can_vote) 


# user = "Piyush"
# True-statement if (condition) else False-statement
# print("Admin" if (user == "Piyush") else "Normal User")
# print(access) 

# user = "Piyush"
# access = "Admin" if (user == "Admin") else ("Super Admin" if (user == "Piyush") else "Normal User")
# print(access)

# LOOPS

# FOR
# for i in range(10):
#     print((i+1)*2)

# FOR WITH RANGE(x, y)
# for i in range(1, 5):
#     print(i)

# NESTED LOOPS AND PATTERNS

# for i in range(5):
#     for j in range(i+1):
#         print("* ", end="")
#     print("")

# for i in range(5):
#     print("* "* (i+1))

# for i in range(5):
#     str = ""
#     for j in range(i+1):
#         str += "*"
#     print(str)

# for i in range(5):
#     print("*" * (i+1))

# import math

# height = 5
# space = math.ceil(height/2)+1

# for i in range(height):
#     print(" " * space + "*" * (i*2 + 1))
#     space -= 1
    
# PRE-POST INC/DEC

# a = 5
# a += 1
# print(a)

# WHILE LOOP

# while True:
#     print("*")

# a = 1
# while a < 5:
#     print(a)
#     a += 1
 
# DO WHILE?

# BREAK & CONTINUE + IF ELSE WITHIN LOOPS
# for i in range(1, 11):
#     if(i%2==1):
#         continue
#     if(i == 7):
#         break
#     print(i)
    
# IF ELSE WITH LOOPS

# for i in range(1, 5):
#     print(i)
#     if(i == 4):
#         break
# else:
#     print("X")

# PASS STATEMENT
i = 2
if(i == 2):
    print("HELLO!")
    # pass
    print("HELLO!")