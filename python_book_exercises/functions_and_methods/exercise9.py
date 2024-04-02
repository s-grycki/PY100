# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# It will print the supplied arguments on seperate lines. Even though the
# function definition has default values for the 2nd and 3rd parameters,
# these are overwritten by passed values
