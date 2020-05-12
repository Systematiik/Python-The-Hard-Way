#def is function, much like methods in java, that allow the user to create mini scripts within scripts

#*args allows the function to take as many arguments given
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#this function allows two arguments to be passed which are arg1, arg2
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this function allows for one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this function takes no arguments
def print_none():
    print("I got nothin\'.")

###These call the functions and applies the arguments into each function###
print_two("Jeremy", "Espino")
print_two_again("Jeremy", "Espino")
print_one("First!")
print_none()