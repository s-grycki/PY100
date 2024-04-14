# Take your code from the previous Check the Weather exercise and rewrite it
# as a match-case statement

from random import choice

options = ('sunny', 'rainy', 'asteroid')
weather = choice(options)

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case _:
        print("Let's stay inside.")
