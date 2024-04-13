# The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, then use the
# resulting error message to determine exactly what is wrong
# (You don't have to fix this code)

# This is the result of trying to concatenate a string with integer 5. This
# tells us that one of the arguments isn't of the type we want
