# How would you print all the numbers in the following range?

range(3, 17, 4)

# Coerce the range into a list and print it
print(list(range(3, 17, 4)))

# This demonstrates that ranges are lazy sequences - they don't generate
# elements until they're needed by the program. The way around this is to
# require the elements via a non-lazy sequence constructor
