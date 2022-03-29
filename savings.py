MONTHLY = 500
INTEREST = 0.10 

amount = 0.0

# after one year
amount = amount + 12*MONTHLY
amount = amount * (1 + INTEREST)

print(amount)