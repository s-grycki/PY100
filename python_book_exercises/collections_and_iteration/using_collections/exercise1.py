# Write Python code to print the seventh number of range(0, 25, 3)

# Proves at least 7 elements by converting to non-lazy sequence
print(list(range(0, 25, 3))) # => [0, 3, 6, 9, 12, 15, 18, 21, 24]

# Gets 7th element out of range iterator
print(range(0, 25, 3)[6]) # => 18
