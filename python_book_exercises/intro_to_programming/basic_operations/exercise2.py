# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

#    One place is 6.
#    Tens place is 3.
#    Hundreds place is 9.
#    Thousands place is 4.

# Each digit may require multiple Python statements.

# Without reassigning original integer
thousands = 4936 // 1000
hundreds = (4936 // 100) % 10
tens = (4936 // 10) % 10
ones = 4936 % 10

print(thousands, hundreds, tens, ones)

# Reassigning original integer
number = 4936
thousands = number // 1000

number = number % 1000

hundreds = number // 100

number = number % 100

tens = number // 10

number = number % 10

ones = number

print(thousands, hundreds, tens, ones)
