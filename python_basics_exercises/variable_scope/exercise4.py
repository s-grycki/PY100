# What will the following code do and why?
# Don't run it until you have tried to answer

a = 1

def my_function():
    print(a) # => 1

my_function()

# All the function does is reference a global variable. In Python, global
# variables are accessible throughout the code
