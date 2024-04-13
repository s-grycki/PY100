# Modify the following code so the loop continues
# iterating until the user inputs 'yes'

# while True:
#     print('Should I stop looping?')
#     answer = input()

while True:
    answer = input('Should I stop looping? ').lower()
    if answer == 'yes' or answer == 'y':
        break
    print('Looping until you say "yes/y".')
