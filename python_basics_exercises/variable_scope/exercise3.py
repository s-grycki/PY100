# What will the following code do and why?
# Don't run it until you have tried to answer

def my_function():
    a = 1

    if True:
        print(a) # => 1

my_function()

# The variable a is initialized in the same scope as where it is being passed
# as an argument to the print function. In fact, it would still work even if
# a were assigned at the global scope because all the function does is
# reference a
