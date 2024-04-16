# What will the following code do and why?
# Don't run it until you have tried to answer

b = [1, 2, 3] # Initializes global variable b

def my_function():
    b[0] = 10 # Reassigns index 0 of global variable b to 10

my_function()
print(b) # => [10, 2, 3]
