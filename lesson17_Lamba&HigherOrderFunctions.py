# lambda function is a single expression that returns a value
squared = lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum_total = lambda a, b: a + b

print(sum_total(5, 10))

##############################

def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

################################
# Higher Order Function
# takes one or more functions as arguments or returns function as result

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers) 
# takes func as argument and iterates through list applying to every value

print(list(squared_nums)) # need to apply list constructor to it

################################

odd_nums = filter(lambda num : num % 2 != 0, numbers)
# filter() filters based on condition, filters out what returns as False
print(list(odd_nums))

################################

from functools import reduce
# apply a function to a sequence of elements and reduce them to a single cumulative value

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)


names = ["Dave Gray", "Sara Ito", "Krish Dhanuka"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)