# Write some code to remove 'fossil' from the list,
# then add 'geothermal' to the end of the list

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

if 'fossil' in energy: energy.remove('fossil') # Handles potential error
energy.append('geothermal')

print(energy) # => ['solar', 'wind', 'tidal', 'fusion', 'geothermal']
