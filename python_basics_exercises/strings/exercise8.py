# Write code that capitalizes the words in the string
# 'launch school tech & talk', so that you get the string
# 'Launch School Tech & Talk'

# Solution 1: Uses list mutation with a for loop
message = 'launch school tech & talk'
message = message.split()

for idx in range(0, len(message)):
    message[idx] = message[idx].capitalize()

message = ' '.join(message)
print(message)



# Solution 2: Uses str.title() method
message = 'launch school tech & talk'
message = message.title()
print(message)
