# What will the following code do and why?
# Don't run it until you have tried to answer

a = 7 # Initializes global variable a

def my_function(b): # Creates local variable b pointing to same value as a
    b += 10 # Reassigns local variable b to new value of 17

my_function(a) # Calls my_function with global variable a as argument
print(a) # => 7
