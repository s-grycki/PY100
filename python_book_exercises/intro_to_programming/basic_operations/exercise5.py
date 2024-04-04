# Will an error occur if you try to access a list element with an index greater
# than or equal to the list's length? For example:

foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?

# Yes. This is because lists start with 0 indexes. A list of length 3 has a max
# index value of 2 - out of range index
