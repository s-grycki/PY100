# Write a function that takes a string as an argument and returns an all-caps
# version of the string when the string is longer than 10 characters.
# Otherwise, it should return the original string.
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def upper_lower(string):
    return (string.upper() if len(string) > 10 else string)

print(upper_lower('hello world'))
print(upper_lower('goodbye'))
