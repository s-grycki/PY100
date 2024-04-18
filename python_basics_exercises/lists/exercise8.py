# How can you check if a variable holds a value that is a list?
# Given two variables, verify whether the values they hold are lists

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

def is_list(object):
    print(type(object) is list)

is_list(some_value1) # => True
is_list(some_value2) # => False
