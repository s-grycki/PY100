# Which of the following values can't be used as a key in a dict object,
# and why?

# 'cat' # => Fine (String)
# (3, 1, 4, 1, 5, 9, 2) # => Fine (Tuple)
# ['a', 'b'] # => Illegal. Keys need to be hashable (lists are mutable)
# {'a': 1, 'b': 2} # => Illegal. Keys need to be hashable (dicts are mutable)
# range(5) # => Fine (Range)
# {1, 4, 9, 16, 25} # => Illegal. Keys need to be hashable (sets are mutable)
# 3 # => Fine (Integer)
# 0.0 # => Fine (Float)
# frozenset({1, 4, 9, 16, 25}) # => Fine (Frozenset)

