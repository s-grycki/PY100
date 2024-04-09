# The following code uses the randrange function from Python's random library
# to obtain and print a random integer within a given range. Using a while
# loop, it keeps running until it finds a random number that matches the last
# number in the range. Refactor the code so it doesn't require two different
# invocations of randrange


# Refactored using a helper function
import random

def random_number(highest):
    return random.randrange(highest + 1)

highest = 10
number = random_number(highest)
print(number)

while number != highest:
    number = random_number(highest)
    print(number)


# Refactored with do/while logic
import random

highest = 10

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

# The do/while solution works better here. Though the helper function abstracts
# logic, there are still technically 2 different invocations returned by the
# method. The do/while solution actually cuts it down to 1 under the logic that
# this will always be run once and we just need to keep returning a random
# number until it meets a break condition
