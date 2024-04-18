# You want to add the numbers from 1 to 5 to a list,
# but the code below is not producing the expected result.
# How can you fix it?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers) # => [0, 1, 2, 3, 4]



# By default, ranges start at 0 and are exclusive with their end points.
# That's why the list output feels shifted backwards. To fix this,
# just specify the start value of 1 and change the end to 6

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers) # => [0, 1, 2, 3, 4]
