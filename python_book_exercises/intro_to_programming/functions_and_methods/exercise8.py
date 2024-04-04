# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# This will raise an error. The function call supplies too many arguments
# 3 were given, but there's only 2 parameters available
