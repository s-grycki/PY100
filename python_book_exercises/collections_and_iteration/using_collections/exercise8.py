# Explain why the code below prints different values on lines 3 and 4

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
# => 'for the fjords' - the first f from right is at index 8

print(text.rfind('f', 21, 35))    # 29
# => 'for the fjords' - the first f from right starting at 21 is 29

# The first example creates a new string by utilizing string slicing.
# The second example uses the original string
