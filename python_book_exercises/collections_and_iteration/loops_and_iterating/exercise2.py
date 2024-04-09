# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter
# The updated code should use a for loop to display the future ages

# Given solution from Input/Output section
# age = int(input('How old are you? '))
# print()
# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

# Refactored with a for loop

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()

for adder in range(10, 50, 10):
    print(f'In {adder} years, you will be {adder + age} years old.')
