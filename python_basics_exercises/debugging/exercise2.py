# Our predict_weather function should output a message indicating whether a
# sunny or cloudy day lies ahead. However, the output is the same every time
# the function is invoked. Why? Fix the code so that it behaves as expected

import random

def predict_weather():
    sunshine = random.choice(['True', 'False']) # => Always truthy

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")



# The error occurs with the assignment to sunshine. Instead of assigning a
# truthy or falsy value, both are non-empty strings, which always evaluate to
# true. This can be fixed by using booleans instead of strings

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()
