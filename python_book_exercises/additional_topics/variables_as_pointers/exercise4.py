# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# Once again, dict2 is a shallow copy of the object referenced by dict1. This
# means that inner objects will be shared even though the outermost objects
# exist at different addresses on the heap. Referencing an inner object will
# impact both variable references, so the mutation of dict1 is reflected in
# dict2
