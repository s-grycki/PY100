# Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?

# Again, the set_foo function call will return None and ignore it
# The print function prints 'bar' because the variable foo within lexical scope
# points to the string 'bar'
