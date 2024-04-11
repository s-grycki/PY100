# What does the following function do? Be sure to identify the output value

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper() # => CHRIS

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict)) # => Prints CHRIS, Returns None

# The function definition is loaded into the heap

# my_dict is loaded into the heap as an object and a pointer is created
# in the stack, with a local variable my_dict referencing the object

# The print function executues and encounters a composition with do_something

# The argument is evaluated as a dictionary object and passed to the function

# do_something calls the sorted function on a dictionary view object of the
# keys, and returns a list with all elements sorted by comparing first
# characters

# Then, it gets index 1, which is now Chris, and uppercases the string as the
# return value

# The print function uses this return value to print the string and return None
