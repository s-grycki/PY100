# In the code shown below, identify all of the function names and parameters
# present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# line 4: multiply, left, right
# line 5: left, right

# line 7: get_num, prompt
# line 8: float, input, prompt

# line 10: get_num
# line 11: get_num
# line 12: multiply
# line 13: print
