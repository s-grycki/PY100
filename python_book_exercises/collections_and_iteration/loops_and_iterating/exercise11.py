# Print all of the even numbers in the following list of nested lists.
# This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

# Solving this requires iteration over collections. Without the for statement,
# I'm forced to use while alongside the independent consideration of list
# length

# Need outer iteration for the 3 elements
# Need inner iteration for the length of the 3 lists
# Need outer and inner indexes to keep track of both

outer_idx = 0

while outer_idx < len(my_list):
    inner_list = my_list[outer_idx]
    inner_idx = 0

    while inner_idx < len(inner_list):
        number = inner_list[inner_idx]
        if number % 2 == 0:
            print(number)
        inner_idx += 1

    outer_idx += 1
