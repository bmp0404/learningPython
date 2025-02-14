class JustNotCoolError(Exception):
    pass


x = 2

try: 
    #print(x/0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
    # raise Exception("I'm a custom exception!")
    raise JustNotCoolError("This just isn't cool")
except NameError:
    print("NameError means undefined")
except ZeroDivisionError:
    print("Please do not divide by zero")
# can find all the names of errors online
except Exception as error:
    print(error)
else:
    print("No errors!")
finally: # happens with or without error
    print("I'm going to print with or without an error")


# need to wrap try block around & need except


