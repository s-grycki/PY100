# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# 42 will be assigned to function local variable first, the second argument
# will overwrite the default value for function local variable second, and
# third will use the default value
