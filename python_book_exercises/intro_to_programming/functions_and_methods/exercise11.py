# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# function local variable first will use the passed value of 42, and second
# and third will use the default values
