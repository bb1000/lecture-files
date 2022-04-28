import argparse
import sys

MONTHLY = 500
INTEREST = 0.10 
RETIREMENT = 70

def main(start_age, stop_age, txt='savings.txt', csv='savings.csv'):
    amount = 0.0
    breakpoint()

    #if len(sys.argv) < 3:
    #    start_age = int(input("Start saving at age: "))
    #    stop_age = int(input("Stop saving at age: "))
    #else:
    #    start_age = int(sys.argv[1])
    #    stop_age = int(sys.argv[2])

    # f = open('savings.txt', 'w')
    f = open(txt, 'w')
    csvfile = open(csv, 'w')
    csvfile.write('age,amount\n')
    for age in range(start_age, RETIREMENT):
        if age < stop_age:
            amount = amount + 12*MONTHLY
        amount = amount * (1 + INTEREST)
        amount = round(amount, 2)
        print(age, amount, file=f)
        print(age, amount, file=csvfile, sep=',')
        
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



    # main(int(sys.argv[1]), int(sys.argv[2]))
    main(args.start_age, args.stop_age, txt=args.save_to_txt, csv=args.save_to_csv)
