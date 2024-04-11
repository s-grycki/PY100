# Use the sqrt function from the math library to write some code that outputs
# the square root of 37. Try to write the code in three different ways

# Plain import
import math
print(math.sqrt(37))

# Import sqrt only
from math import sqrt
print(sqrt(37))

# Import math with alias
import math as m
print(m.sqrt(37))
