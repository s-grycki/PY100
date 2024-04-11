# In your own words, explain the difference between these two expressions

# my_object1 == my_object2
# my_object1 is my_object2

import copy

# == is checking for value equivalency between objects. For example,
# 2 different lists containing the same values will evaluate as true despite
# being different objects existing at different memory locations on the heap
my_list = ['A', [2, 3, ['d4']], 5]
dup = copy.copy(my_list)

print(my_list == dup)             # => True. Different lists of same values
print(my_list[1] == dup[1])       # => True. Same values
print(my_list[1][2] == dup[1][2]) # => True. Same values

print(my_list is dup)             # => False. These are 2 different list objects
print(my_list[1] is dup[1])       # => True. Shallow copy
print(my_list[1][2] is dup[1][2]) # => True. Shallow copy



# is checks if both sides of the keyqord reference the same object, despite if
# they contain the same values. Do the objects exist at the same memory
# location on the heap?
my_list = ['A', [2, 3, ['d4']], 5]
dup = copy.deepcopy(my_list)

print(my_list == dup)             # => True
print(my_list[1] == dup[1])       # => True
print(my_list[1][2] == dup[1][2]) # => True 

print(my_list is dup)             # => False. These are different list objects
print(my_list[1] is dup[1])       # => False. Deep copy
print(my_list[1][2] is dup[1][2]) # => False. Deep copy

# The variables in both examples point to different stack locations
# The stack locations in both examples point to different outer heap addresses
# The first example has pointers to the same inner heap addresses
# The second example has pointers to different inner heap addresses
