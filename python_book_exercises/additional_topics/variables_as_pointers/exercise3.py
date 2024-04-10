# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# The dict constructor will create a shallow copy of the argument since they're
# objects of the same type. When the mutation of key/value assignment occurs
# with dict2, it will not impact dict1 since the outermost heap level
# references different objects. The print function results in the original
# value being printed
