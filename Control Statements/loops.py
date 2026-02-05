# for loop
for i in range(1, 5):
    # Prints from 1 to 4.
    print(i)

print()

for i in range(10):
    # Prints from 0 to 9.
    print(i)
    
print()    

# while loop
i = 1
while i < 5:
    print(i)
    i+=1

print()

# infinite loop safe guard with break 
i = 1
while True:
    print(i)
    i += 1
    if i == 2:
        break
    
print()

# continue statement
for i in range(11):
    if i % 2 == 0:
        continue
    print(i)
    
print()
    
# if-else with loops
for i in range(5):
    if i == 10:
        break
else:
    print("Break was not found.")    
    
print()
    
# The pass statement
if True:
    print("I am writing...")
    pass
else:
    print("Hey!")