# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# Nothing. The function will encounter an explicit return with no argument, so
# it exits and returns to the calling expression before the print function
