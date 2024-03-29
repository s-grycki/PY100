# Repeat the previous question but, this time, use augmented assignment to
# compute the final result, one year at a time.

# Same as last answer:
balance = 1_000

for i in range(0, 5):
    balance *= 1.05

print(f'${round(balance, 2)}')
