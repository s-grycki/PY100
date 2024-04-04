# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) # => Empty

# This function is evaluating the truthiness of an empty list. In Python,
# empty collections/strings evaluate to false. Therefore, the else block
# will be executed
