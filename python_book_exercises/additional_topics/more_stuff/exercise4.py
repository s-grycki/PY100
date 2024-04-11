# Write a function called increment_counter that increments a counter variable
# every time it is called

def increment_counter():
    global counter
    #print(counter)
    counter += 1
    #return counter

counter = 0

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

# This solution was looking for a function taking no arguments and demonstrates
# some behaviors I see as wonky in Python. Even without the global keyword, the
# function is still able to access the variable counter defined at the global
# scope. Yet, if we try to reference counter before reassignment, then Python
# throws an error because it's trying to reference a locally scoped variable
# before it was defined

# Also of note, we don't need to return a value here. We're only looking to
# increment the global variable
