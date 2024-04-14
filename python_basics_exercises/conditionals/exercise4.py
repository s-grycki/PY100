# Initialize a variable weather with a string value being 'sunny', 'rainy', or
# whatever weather condition you choose.
# Then, write an if statement that prints:

#    It's a beautiful day! if weather's value is 'sunny'
#    Grab your umbrella. if weather's value is 'rainy'
#    Let's stay inside. if weather's value is anything else

# Test your code with different values for weather

from random import choice

options = ('sunny', 'rainy', 'asteroid')
weather = choice(options)

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print('Grab your umbrella.')
else:
    print("Let's stay inside.")
