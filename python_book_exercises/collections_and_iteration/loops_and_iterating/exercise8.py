# Write a comprehension that creates a dict object whose keys are strings and
# whose values are the length of the corresponding key
# Only keys with odd lengths should be in the dict
# Use the set given by my_set as the source of strings

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

def is_odd(string):
    return len(string) % 2 != 0

my_dict = { key : len(key)
            for key in my_set
            if is_odd(key) }

print(my_dict)
