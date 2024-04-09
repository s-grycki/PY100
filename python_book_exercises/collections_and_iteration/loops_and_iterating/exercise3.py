# Use a while loop to print the numbers in my_list, one number per line
# Then, do the same with a for loop

my_list = [6, 3, 0, 11, 20, 4, 17]


# While loop
index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1


# For loop
for item in my_list:
    print(item)

# The for loop works better here because we know how many times we want to
# iterate. In this case, the whole length of a collection. Also, for loops
# work well with collections due to the implied element access
