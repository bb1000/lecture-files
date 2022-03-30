import sys

MONTHLY = 500
INTEREST = 0.10 
RETIREMENT = 70

amount = 0.0

if len(sys.argv) < 3:
    start_age = int(input("Start saving at age: "))
    stop_age = int(input("Stop saving at age: "))
else:
    start_age = int(sys.argv[1])
    stop_age = int(sys.argv[2])

for age in range(start_age, RETIREMENT):
    if age < stop_age:
        amount = amount + 12*MONTHLY
    amount = amount * (1 + INTEREST)
    amount = round(amount, 2)
    
print("Savings at age", age, amount)
