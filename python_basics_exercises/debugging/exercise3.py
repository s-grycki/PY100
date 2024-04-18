# When the user inputs 10, we expect the program to print The result is 50!,
# but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5 # => Returns string

print("Hello! Which number would you like to multiply by 5?")
number = input() # => Returns a string

print(f"The result is {multiply_by_five(number)}!") # => 1010101010



# A string object is being passed into the function. This is causing string
# duplication. In order to fix this, we should convert the input to an integer
# at the variable decleration, the function call, or in the function itself

def multiply_by_five(n):
    return n * 5 # => Returns integer

print("Hello! Which number would you like to multiply by 5?")
number = int(input()) # => Returns integer

print(f"The result is {multiply_by_five(number)}!") # => 50
