import csv

fn = 'budget_data.csv'
ofn = 'results.txt'
fhandler = open(fn)
out_fhandler = open(ofn,'w')

reader = csv.reader(fhandler)
header = next(reader)

months = 0
net_total = 0
delta_total = 0
max_increase = None
max_increase_date = None
max_decrease = None
max_decrease_date = None
previous = None


for date,profit in reader:
    profit = int(profit)
    months += 1
    net_total += profit

    if previous is not None:
        delta = profit - previous[1]
        delta_total += delta
        if max_increase is None or delta > max_increase:
            max_increase = delta
            max_increase_date = date
        if max_decrease is None or delta < max_decrease:
            max_decrease = delta
            max_decrease_date = date
    previous = (date,profit)

output = \
f"""Financial Analysis
-------------------------
Total Months: {months}
Total: ${net_total}
Average Change: ${delta_total/(months-1):.2f}
Greatest Increase in Profits: {max_increase_date} ({max_increase})
Greatest Decrease in Profits: {max_decrease_date} ({max_decrease})
"""

print(output)
out_fhandler.write(output)