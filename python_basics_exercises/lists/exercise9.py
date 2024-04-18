# Write a function that, without using the built-in in operator,
# checks whether a specific destination is included within destinations.
# For example: When checking whether 'Barcelona' is contained in destinations,
# the expected output is True, whereas the expected output for 'Nashville'
# is False

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(destination, destinations):
    for city in destinations: # => not in operator. Part of for loop syntax
        if city == destination:
            return True

    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
