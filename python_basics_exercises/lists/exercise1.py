# Write a function that returns the first element
# of a list provided as an argument

# Be sure to handle the case where the input list is empty

def first(list_object):
    return list_object[0] if list_object else None

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))                         # None
