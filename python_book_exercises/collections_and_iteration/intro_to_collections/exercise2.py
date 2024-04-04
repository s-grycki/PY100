# Can you write some code to change the value 'bye' in the following tuple to
# 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# No. Tuples are immutable. We would have to create a new tuple

# Creates a slice from 0 to index - 1, and then concatenates a tuple
stuff = stuff[0:2] + ('goodbye', stuff[3])
print(stuff)

# Constructs a list from tuple iterable since lists are mutable
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)
