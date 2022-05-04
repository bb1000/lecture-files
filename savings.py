import argparse

MONTHLY = 500
INTEREST = 0.10 
RETIREMENT = 70


class SavingsCalculator:

    def __init__(self, start_age, stop_age, txt='savings.txt', csv='savings.csv'):
        self.start_age = start_age
        self.stop_age = stop_age
        self.txt = txt
        self.csv = csv
        self.savingsdata = []

    def main(self):

        amount = 0.0
    
        for age in range(self.start_age, RETIREMENT):
            if age < self.stop_age:
                amount = amount + 12*MONTHLY
            amount = amount * (1 + INTEREST)
            amount = round(amount, 2)
            self.savingsdata.append((age, amount))

    def to_txt(self):
        f = open(self.txt, 'w')
        for age, amount in self.savingsdata:
            print(age, amount, file=f)
        f.close()

    def to_csv(self):
        csvfile = open(self.csv, 'w')
        csvfile.write('age,amount\n')
        for age, amount in self.savingsdata:
            print(age, amount, file=csvfile, sep=',')
        csvfile.close()

    def final(self):
        age, amount = self.savingsdata[-1]
        print("Savings at age", age, amount)
        return amount

# print('__name__ =',__name__)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('start_age', type=int)
    parser.add_argument('stop_age', type=int)
    parser.add_argument('--save-to-txt', default='savings.txt', help='text file for savings data')
    parser.add_argument('--save-to-csv', default='savings.csv', help='csv file for savings data')
    parser.add_argument('--interest', default=INTEREST, type=float)
    args = parser.parse_args()
    print(args)
    print(args.start_age)
    print(args.stop_age)

    savings_calculator = SavingsCalculator(args.start_age, args.stop_age, txt=args.save_to_txt, csv=args.save_to_csv)
    final_amount = savings_calculator.main()
