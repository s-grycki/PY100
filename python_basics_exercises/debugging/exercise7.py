# You are trying to access a value in a dictionary,
# but the code is giving you an error.
# Can you change line 3 so that it prints "Unknown"
# instead of raising an error?

info = {'name': 'Srdjan', 'age': 38}

# print(info['city']) # => KeyError (city doesn't exist)



# By default, Python will return an error if we try accessing a value from a
# dictionary with a non-existant key. To get around this, we could use a
# ternary or the .get() method for dictionaries

print(info['city'] if 'city' in info else 'Unknown')
print(info.get('city', 'Unknown'))
