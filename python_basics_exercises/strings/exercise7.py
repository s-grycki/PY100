# Write an is_empty_or_blank function to determine whether a string
# is either empty or consists entirely of spaces

# Solution 1
def is_empty_or_blank(string):
    return not string or string.isspace()

# Solution 2
def is_empty_or_blank(string):
    return not s.strip(' ')

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
