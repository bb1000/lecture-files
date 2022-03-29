MONTHLY = 500
INTEREST = 0.10 

amount = 0.0


for age in range(20, 25):
    amount = amount + 12*MONTHLY
    amount = amount * (1 + INTEREST)
    amount = round(amount, 2)
    
    print("Savings at age", age, amount)