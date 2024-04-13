# Find the Python Documentation on operator precedence, and use it to
# determine the result of evaluating 4 * 5 + 3**2 / 10

# Python Language Reference => Expressions => Operator precedence

print(4 * 5 + 3**2 / 10) # => 20.9

# Better to use paranthesis for clarity
print((4 * 5) + ((3**2) / 10)) # => 20.9
