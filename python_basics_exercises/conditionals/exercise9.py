# Without running the following code, determine what will be printed

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}") # => $3.99

# The not keyword negates the boolean evaluation. Logically, it's like we're
# checking truthiness in the reverse order usually expected
