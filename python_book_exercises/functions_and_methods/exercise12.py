# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# This will return an error. The function definition has 2 parameters with
# default values, but the first lacks a default value. To fix this, we could
# supply a single argument, or ideally, give first a default value
