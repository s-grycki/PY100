# The following function returns a list of the remainders of dividing the
# numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain
# any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # [0,1,2,3,4,0,1,2,3,4,0] False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9] # [1,2,3,4,1,2,3,4] True
numbers_3 = [0, 5, 10] # [0,0,0] False
numbers_4 = [] # [] True (technically)

# If any element in returned list is 0, then it should return false
# Not checking if any element in list is truthy

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))

# all because we want all integers to be non-zero
# all works with an empty list because none of the values contained are falsy
# any would return false because no value evaluates to true
