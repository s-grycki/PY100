# What will the following code do and why?
# Don't run it until you have tried to answer

a = 1 # => Initialize globally scoped variable a

def my_function():
    a = 2 # => Initialize locally scoped variable a

my_function() # => Return None
print(a) # => 1
