users = ["krish", "bob", "ryan"]
data = ["krish", 18, True] # not limited to singular data type
emptylist = []

# Indexes
print(users[0])
print(users[-1])
print(users[0:2])
print(users[0:])
print(users[-3:-1])
print(users.index("krish"))

# List Methods
print(len(users))
print("krish" in users)

# Adding to list
users.append("alex")

# combining lists
users += ["hello"] # needs to be list and not string for +=
users.extend(["goodbye, peace"])

data.clear()
users.extend(data)


# Adding to start/specific spot
users.insert(0, "bobbyj")
users[2:2] = ["Eddie", "Alex"]

# Replacing in list
users[1:3] = ["JP", "TJ"] # replaces spot 1 & 2

# Removing from list
users.remove("JP") # specific remove
users.pop() # removes last spot and returns what was popped
del users[0] # deletes range of spots
# del data # perma deletes list
data.clear() # clears list

# Sorting list - lowercase comes after uppercase by default
users.sort()
users.sort(key=str.lower) # ignores case

# New List
nums = [4, 42, 23, 12, 35]
nums.reverse()

# Sorting in reverse
nums.sort(reverse = True)

# Want to keep original list & not modify it
print(sorted(nums, reverse = True)) # does not modify list

# Ways to create copies
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

# Checking type of list
type(nums)

# Using list constructor
mylist = list([1, "neil", True])






# Tuples: data inside does not change & order of data does not change
mytuple = tuple(("dave", 42, False))
anothertuple = (1, 4, 2, 8) # packing a tuple
print(type(anothertuple))

newlist = list(mytuple) # creates list out of tuple
newlist.append("neil")
newtuple = tuple(newlist) # converts list back into tuple but w/added thing

(one, two, *hey) = anothertuple # unpacking a tuple, data -> variables
print(one)
print(two)
print(hey) # star puts rest of data in list form in that variable

# Tuple Methods
anothertuple.count(2) # number of occurences of parameter









