# The following code causes an infinite loop
# (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# This is just going to keep printing 0 because the counter is never
# incremented. The while condition will always be truthy. Adding counter += 1
# to the final line of the block would fix this
