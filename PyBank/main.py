import os
import csv
import statistics

csvpath = os.path.join('Resources', 'budget_data.csv')

# Defining lists to store values
date = []
revenue = []
profit_history = []

# Open csv file
with open(csvpath) as csvfile:
# Declares how the csv file should be read
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
# Define sum_revenue to add up values of revenue list
    def sum_revenue(csvreader):
        total = 0
        for row in csvreader:
            total = int(total) + int(row)
        return total
# for loop to add values of date and revenue
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1]) 

for i in range(len(revenue)):
    change = int(revenue[i-1]) + (1 - int(revenue[i]))
    profit_history.append(change)

# for i in range(len(revenue)):
#     c1 = revenue[i]
#     c2 = revenue[i-1]
#     change = int(c1) + int(c2)
#     profit_history.append(change)
#     c1, c2 = 0, 0

neg_profit = list(filter(lambda profit_history:profit_history<0,profit_history))
pos_profit = list(filter(lambda profit_history:profit_history>0,profit_history))

profit_change = statistics.mean(pos_profit)+statistics.mean(neg_profit)

total_change = profit_change / len(profit_history)

months = len(date)
total_sum = sum_revenue(revenue)
min = min(profit_history)
max = max(profit_history)

# print(revenue)
# print(profit_history)
       
print(
    "------------------------------ \n"
    "Financial Anaylsis \n"
    "------------------------------ \n"
    f'Total Months: {months} \n'
    f'Total: $ {total_sum} \n'
    f'Average Change: {total_change} \n'
    f'Greatest Increase in Profits: $ {max} \n'
    f'Greatest Decrease in Profits: $ {min} \n'
    )
