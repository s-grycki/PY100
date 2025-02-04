# Python lists come with a variety of built-in methods that allow for common
# list manipulations. One such operation is determining the index of an item
# in the list

# Given a list:
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

# How would you determine the index of the fruit "cherry" in this list?

if 'cherry' in fruits:
    print(fruits.index('cherry'))

# This is found under common sequence operations, meaning that both mutable and
# immutable sequences can use this method, not just lists
