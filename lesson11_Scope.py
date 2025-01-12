
name = "Dave" # global scope

def greeting(name):
    color = "blue" # local scope of function
    print(name) # prints local scope and not global scope variable 
    print(color)

greeting("John")

def another(): 
    greeting("dave")

another() 

def another2():
    color = "blue"
    def greeting2(): # define functions inside another function but can't be called outside
        print(color) # able to access variables in local scope of parent function

# try to keep global scope as unpolluted as possible and keep everything inside local (functions, classes, etc)

count = 1

def another3():
    # count = 2 # creates new variable count in local scope
    global count # allows you to access global variable
    count += 1 # can't modify without using global keyword
    print(count)

another3()

# for same situation but with parent function variable, use keyword "nonlocal"
def hello():
    hhh = 10
    def hello2():
        nonlocal hhh
        hhh += 2
        print(hhh)
    hello2()

hello()

