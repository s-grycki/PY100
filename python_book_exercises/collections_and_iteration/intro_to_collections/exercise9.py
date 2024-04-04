my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

#     Are the lists assigned to my_list and another_list equal?
#     Are the lists assigned to my_list and another_list the same object?
#     Are the nested lists at index 3 of my_list and another_list equal?
#     Are the nested lists at index 3 of my_list and another_list the same object?

# Don't write any code for this exercise.

# 1. Yes. They will hold equivalent values of the same object. The list 
# constructor creates a shallow copy of the argument
# (== comparision will be true)

# 2. No. This is creating a copy of the list by creating a new object in
# memory (is comparison will be false)

# 3. Yes. They are lists of equivalent values
# (== comparision will be true)

# 4. Yes. This is a shallow copy, which means only the referenced object
# itself is different (is comparison will be true)
