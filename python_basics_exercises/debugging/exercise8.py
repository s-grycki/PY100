# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game.
# However, we encountered an issue, as whenever we change a value in one nested list,
# all nested lists are affected. Can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]



# In this program, a for loop is created with the sole purpose of iterating
# 3 times. On each iteration, the list pointed to by matrix will be populated
# with the object pointed to by sub_list. Therefore, when we mutate any
# element within matrix, it will impact all 3 references to the same object.
# In order to get around this, we want to append a different object each time
# with the same value as sub_list. This is where creating a copy
# comes in handy. In this case, a shallow copy will do since all elements
# inside the list are immutable

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list[:]) # => Shallow copy of list

matrix[0][0] = "X" # => Mutates list; reassigns element
print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
