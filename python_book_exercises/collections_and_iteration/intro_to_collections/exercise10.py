# Bob expects the following code to print the names in alphabetical order.
# Without running the code, can you say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

# Maybe, but probably not. Sets are unordered collections, so there's no way to
# predict order. The closest compramise would be to use a tuple, since like
# sets, they're immutable collections, but they're also sequences which can
# be sorted
