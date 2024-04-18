# Predict the output of the code shown below. When you run the code,
# do you see what you expected? Why or why not?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2) # => True

# Lists are sequences, and the == operator checks for value equivalency, not
# for object equivalency. This means that as long as 2 different lists have
# equal values in their respective indexes, the above will return True
