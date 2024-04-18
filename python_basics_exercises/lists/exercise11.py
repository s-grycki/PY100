# We have a grocery list. As we check off items on that list,
# we want to remove them from the list

# Write code that removes the items from grocery_list, one by one,
# until it is empty. If you print the elements you remove,
# the expected behavior would look as follows



# Solution 1: For loop iterating length times
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

for _ in range(0, len(grocery_list)):
    print(grocery_list[0])
    grocery_list.remove(grocery_list[0]) # => Returns None

print(grocery_list)



# Solution 2: Relying on the truthiness of a non-empty list
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']
    
while grocery_list:
    checked_item = grocery_list.pop(0) # => Returns deleted item
    print(checked_item)

print(grocery_list)

# Expected output
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []
