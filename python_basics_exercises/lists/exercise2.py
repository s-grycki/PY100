# Write a function that returns the last element
# of a list provided as an argument

# Be sure to handle the case where the input list is empty

def last(list_object):
    return list_object[-1] if list_object else None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))                         # None
