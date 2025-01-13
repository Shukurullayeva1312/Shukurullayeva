def invest(amount, rate, years):
    i = 1
    for i in range(years):
        final_amount = amount * pow(((1 + rate / 100)), i)
        print('year', i, ': ', round(final_amount, 2))
#invest(amount, rate, years)
#invest(100, 5, 6)
amount = float(input('enter initial amount: '))
rate = float (input('enter an annual rate in percentages: '))
years = int(input('enter a number of years: '))
invest(amount, rate, years)