# The following function returns a list of the remainders of dividing the
# numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at least
# one number that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []





# Returns new list and evaluates any function on it
print(any(remainders_3(numbers_1))) # True
print(any(remainders_3(numbers_2))) # True
print(any(remainders_3(numbers_3))) # False
print(any(remainders_3(numbers_4))) # False

# This works because 0 is falsy in Python

# Falsy values in Python: Empty sequences, strings, and sets, the numeric zero,
# None, and boolean False

# Different from Ruby where only False and nil are falsy

# The above function isn't intended as a predicate method, so this is why any
# is used outside of it
