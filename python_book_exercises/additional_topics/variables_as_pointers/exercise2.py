# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# This creates 2 different variables in memory which point to different stack
# locations, but these addresses in the stack point to the same heap addresses
# which are storing objects. Therefore, when the add method is called to one
# pointer, it will impact both references since this is a mutating method
