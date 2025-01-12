person = "Dave"
coins = 3

# old way of formatting strings
# concatenating with plus signs
print("\n" + person + " has " + str(coins) + " coins left.")

# percent method
message = "\n%s has %s coins left." % (person, coins) 
print(message) # inserts person at first %s & coins at second %s

# format method
message = "\n{} has {} coins left.".format(person, coins) 
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message) # putting index positions

message = "\n{person} has {coins} coins left.".format(person = person, coins = coins) 
print(message) # using variable names

player = {'person': 'Dave', 'coins': 3}
message = "\n{person} has {coins} coins left.".format(**player) 
print(message) # using dictionary


############
# f-Strings

message = f"\n{person} has {coins} coins left."

message = f"\n{person} has {2 * 5} coins left." # can use operations inside

message = f"\n{person.lower()} has {2 * 5} coins left." # can use methods inside 

message = f"\n{player['person']} has {player['coins']} coins left." # using dictionary
print(message)

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}") #:.2f is for formatting, .2 = 2 decimal spot

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}") # % adds percent output


