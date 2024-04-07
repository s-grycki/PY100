# Write Python code to replace all the : characters in the string below with +

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# Converting to list and mutating elements

info_list = list(info)

for elem in range(0, len(info_list)):
    if info_list[elem] == ':':
        info_list[elem] = '+'

info = ''.join(info_list)
print(info) # => xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh



# Alternatively, we could work with a new string while iterating over each
# character in the original. This actually uses a bit less logic

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = ''

for elem in info:
    if elem != ':':
        new_info += elem
    else:
        new_info += '+'

print(new_info) # => xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh



# Using the split method

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info = info.split(':')
info = '+'.join(info)
print(info) # => xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh



# Using the replace method

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

print(info.replace(':', '+')) # => xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh
