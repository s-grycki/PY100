# What will the following code do and why?
# Don't run it until you have tried to answer

a = 1 # => Initializes global variable a

def my_function():
    print(a) # => Causes error. The function has local variable a now
    a = 2 # => Creates new local variable a

my_function()

# Python reads the function definition and knows that it has a locally
# scoped variable of a. However, the function tries to access this variable
# before it is assigned a value when the function is run
