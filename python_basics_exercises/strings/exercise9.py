# Write a function that checks whether a string starts with a specific prefix

# Solution 1: Using string slicing
def starts_with(string, prefix):
    substring = string[0:len(prefix)]
    return substring == prefix

# Solution 2: Using str.startswith()
def starts_with(string, prefix):
    return string.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
