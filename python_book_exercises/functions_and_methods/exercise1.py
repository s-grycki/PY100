# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# set_foo is called and this function has no explicit return value, so None is
# returned and ignored
# the print function will return an error because the argument foo is a local
# variable which was initialized inside of the function scope
