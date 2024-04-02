# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# This will raise an error. The first problem is that the function definition
# has a default value for the middle parameter, but a subsequent parameter has
# no deafult value. This isn't allowed in Python. Even if we somehow get past 
# this, the function is expecting 3 values, but would only have 2 to work with
