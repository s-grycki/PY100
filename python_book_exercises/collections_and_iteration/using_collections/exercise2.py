# Use slicing to write Python code to print a 6-character substring of
# 'Launch School' that begins with the first c

# Locates index at first instance of c
start_index = ('Launch School'.find('c')) # => 4

# Gets 6 character string slice
print('Launch School'[start_index : start_index + 6]) # => 4 : 10, 'ch Sch'
