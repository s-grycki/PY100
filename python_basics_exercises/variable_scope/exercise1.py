# What will the following code do and why?
# Don't run it until you have tried to answer

if True:
    my_value = 20

print(my_value) # => 20

# A code block doesn't always imply a new local scope for variables.
# If statements are examples of this



# What do you think will happen if we run the following code instead:

if False:
    my_new_value = 42

print(my_new_value) # => Undefined variable error

# The variable is accessible, but was never pointed to a value
