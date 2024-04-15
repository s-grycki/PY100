# Use Python's string methods on the string 'Captain Ruby'
# to create a string with the value 'Captain Python'

# String slicing
message = 'Captain Ruby'
message = message[:8] + 'Python'
print(message)

# Substring replacement
message = 'Captain Ruby'
message = message.replace('Ruby', 'Python')
print(message)

# Splitting into list elements
message = 'Captain Ruby'
message = message.split(' ')[0] + ' Python'
print(message)
