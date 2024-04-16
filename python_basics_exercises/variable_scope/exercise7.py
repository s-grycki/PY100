# What will the following code do and why?
# Don't run it until you have tried to answer

a = 1 # => Initialize global variable a

def my_function():
    global a # => Allow access to global variable a like a local variable
    a = 2 # => Reassigns global variable a to 2

my_function() # => Returns None
print(a) # => 2
