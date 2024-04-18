# Your colleague has implemented a custom function to find the maximum value in a list.
# However, the function sometimes works correctly, but other times it produces incorrect results.
# Can you help your colleague fix the bug?

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = 0 # => Creates problems if list has no positive numbers
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2



# The first 2 cases work fine, but setting the max_number to 0 creates
# problems with the conditional as is. Setting the current max to the first
# element and then iterating through would fix this

def find_maximum(numbers):
    if not numbers: return None

    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2
