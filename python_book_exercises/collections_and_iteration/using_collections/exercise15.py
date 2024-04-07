# Without running the following code, what values will be printed by
# the final line?

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
# => dictionary view object of keys. dict_keys(['Cat', 'Dog', 'Bird'])

del pets['Dog']
# => deletes key/value pair. {'Cat': 'Meow', 'Bird': 'Tweet'}

pets['Snake'] = 'Sssss'
# => adds new key/value pair to end of dictionary. 'Snake': 'Sssss'

print(keys)
# => dict_keys(['Cat', 'Bird', 'Snake'])

# The reason that the updated list of keys is printed instead of the original
# when keys was assigned is due to keys being a dictionary view object. Any
# changes made to the referenced dictionary will be reflected in real-time.
# These aren't independent lists, they're tied to the state of an object
