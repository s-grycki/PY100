# In the following code snippet, find all violations of the PEP8 style guide
# Rewrite it so that it conforms with the guide

# iceCreamDensity=10
# 
# while iceCreamDensity>0 :
#     print('Drip...')
#     iceCreamDensity-=1
# 
# print('The ice cream melted.')



ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

# This violates the following proposals:
# that binary operators should have a single space on either side. In PEP8:
# Whitespace in Expressions and Statements => Other Recomendations => Point 2

# Initializing variable names in PascalCase instead of snake_case. In PEP8:
# Naming Conventions => Prespective: Naming Conventions =>
# Function and Variable Names

# Putting a space before the colon with the while loop. In PEP8:
# Whitespace in Expressions and Statements => Pet Peeves => Point 3

