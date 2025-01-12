# While Loops

# value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break # can stop loops with break statement
#     value += 1

# value2 = 1
# while value2 < 10:
#     value2 += 1
#     if value2 == 5:
#         continue # goes to next iteration of loop so doesn't print 5
#     print(value2)
# else: # executes when loop complete if break is not used
#     print("value = " + str(value2)) 


# For Loops
names = ["krish", "bob", "alex"]
# for x in names:
#     print(x)

for x in "Mississippi":
    print(x)

for x in names:
    if x == "bob":
        break
    print(x)

for x in range(4): # starts at 0 & ends at 4, returns 0,1,2,3
    print(x)

for x in range(2, 4): # starts at 2 & ends at 4, so returns 2,3
    print(x)

for x in range(0, 100, 5): # starts at 0, ends at 100, inc by 5
    print(x) # prints 0 -> 95 adding 5 each time
else:
    print("glad that is over")

# Nested for loops
names = ["krish", "bob", "alex"]
actions = ["codes", "eats", "sleeps"]

for name in names: 
    for action in actions:
        print(name + " " + action + ".")





    



