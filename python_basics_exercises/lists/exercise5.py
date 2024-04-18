# Count the number of elements in scores that are 100 or above

scores = [96, 47, 113, 89, 100, 102]

# Solution 1: Using a for loop
count = 0

for score in scores:
    if score >= 100: count += 1

print(count)

# Solution 2: Using a list comprehension
count = len([score for score in scores if score >= 100])
print(count)
