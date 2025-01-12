# function names need to be all lowercase, use underscores for separating
def hello():
    print("hello world")

hello()

# functions w/parameters
def sum(num1, num2=3): # =3 adds default value if no param typed for num2
    if (type(num1) is not int or type(num2) is not int):
        return # returns none
    return num1 + num2

total = sum(2, 3)


def multiple_items(*args): # unknown number of parameters, * returns tuple
    print(args)
    print(type(args))

multiple_items("dave", "john", "krish")

def mult_named_items(**kwargs): # ** returns dictionary, need to name arguments
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "krish", last = "dude")





