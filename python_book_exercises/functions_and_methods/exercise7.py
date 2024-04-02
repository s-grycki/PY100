# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# This will raise an error. The foo function expects 2 arguments, but only one
# is supplied with the function call. The way around this would be to assign
# a default value to the 2nd parameter or add a 2nd argument
