# What will the following code do and why?
# Don't run it until you have tried to answer

x = 10 # => Global scope

def my_function(): # => Creates function scope
    x = x + 5 # => This causes an error
    print(x)

my_function()

# There will be an error because functions create new scoping rules.
# In python, we could reference or mutate x (assuming it's a mutable type),
# but with reassignment, Python is expecting a local variable to already be
# available in the proper scope. That's not the case here. Potential solutions
# are using the global keyword, passing x as an argument, or creating a new
# locally scoped x variable
