# Dictionaries

band = {
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals = "plant", guitar = "page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Accessing Items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# Verify a key exists
print("guitar" in band) # True
print("triangle" in band) # False

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass")) # returns "JPJ"
print(band.popitem()) # returns last added key/value as a tuple

# Add items
band["drums"] = "Bonham"

# Delete & clear
del band["drums"] # deletes key/value pair
band2.clear() # clears dictionary entirely
del band2 # completely deletes dictionary

# Copy dictionaries
band2 = band # Creates reference, editing band also edits band2 & vice versa
# Bad Copy ^^^
# How to create copy
band2 = band.copy() # does not do same reference
# Good Copy ^^^
# or use dict() constructor function
band3 = dict(band)
# Good Copy ^^^


# Nested Dictionary (value is another dictionary)
member1 = {
    "name":"plant",
    "instrument":"vocals"
}
member2 = {
    "name":"page",
    "instrument":"guitar"
}

bandband = {
    "member1": member1,
    "member2": member2
}
print(bandband)
print(bandband["member1"]["name"]) # getting specific value, returns plant







# Sets, no duplicates allowed
nums = {1, 2, 3, 4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

numsnums = {1, 2, 2, 3}
print(numsnums) # removes duplicates
# True is a dupe of 1, False is a dupe of 0
numstest = {1, True, 2, False, 3, 4, 0} # true not in set but false is bc before 0
print(numstest)

# Check if a value is in a set
print(2 in numsnums)
# cannot refer to element in set with an index position or key

# Adding values to sets
numsnums.add(8)

# Adding sets from one set to another
morenums = {5, 6, 7}
numsnums.update(morenums) # combines both sets

# You can use update with lists, tuples, and dictionaries

# Merge two sets to create a new set
setone = {1, 2, 3}
settwo = {5, 6, 7}
mynewset = setone.union(settwo)

# Keeping only duplicates of sets
oneset = {1, 2, 3}
twoset = {2, 3, 4}
oneset.intersection_update(twoset) # changes first set "oneset" to only have duplicates

# Keeping only nonduplicates
oneset = {1, 2, 3}
twoset = {2, 3, 4}
oneset.symmetric_difference_update(twoset) # changes first set "oneset" to only have nonduplicates







