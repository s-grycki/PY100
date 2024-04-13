# Using the code below as a starting point, write a while loop that prints
# the elements of lst at each index and terminates after printing the last
# element of the list

lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1



# Further Exploration
# What would the code output if lst is empty? Why is that?

# Nothing would happen because the while loop would never run. However, if it
# did, then there would be an error because the code would be trying to access
# index values which are out of range
