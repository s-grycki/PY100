# Is there a method to reverse a string,
# for example turning 'hello' into 'olleh'?

# There isn't a specific method for reversing strings in Python, but a way
# around this is by using a list constructor on the string and using the
# reverse method for this class, and then joining the object back into a
# new string

name = 'Shawn'
list_name = list(name)
list_name.reverse()
name = ''.join(list_name)
print(name)

# Using string slicing instead
name = 'Shawn'
name = name[::-1]
print(name)
