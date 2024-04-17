# Write a function that counts the number of occurrences
# of a substring in a string

# Solution 1: Using string.find() with while loop
def count_substrings(string, substring):
    count = 0
    start_idx = 0

    while start_idx < len(string):
        end_idx = string.find(substring, start_idx)
        if end_idx != -1:
            count += 1
            start_idx = end_idx + len(substring)
        else:
            break
    return count



# Solution 2: Using string.count()
def count_substrings(string, substring):
    return string.count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
