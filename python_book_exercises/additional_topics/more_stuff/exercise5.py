# On reflection, we've decided that we don't want to rely on using a global
# variable in the code we wrote in the previous example. To fix this, we're
# going to nest the code from the previous example into an outer function:

def all_actions():
    counter = 0

    def increment_counter():
        #global counter
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

# There's a bug in this code. Identify the bug, and fix it

# The bug is using the global keyword. Originally, this was trying to reference
# non-existant global variable of counter, which caused an error when trying to
# increment. nonlocal will search the outerscopes for a matching variable and
# allow local access to this variable

# It's tempting to just use arguments here, but it wont work because this will
# just create a new locally scoped counter variable which adds 1 to the
# originally passed variable. Hence, the original counter would never increment
