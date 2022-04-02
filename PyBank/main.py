import os
import csv

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

# def add(i):
#     num = 0
#     for i in range(0, len(profit_history)):
#         num = num + profit_history[i]
#     return num


months = len(date)
total_sum = sum_revenue(revenue)

min = min(profit_history)
max = max(profit_history)
total_change = sum(profit_history)
average_change = (max - min) / total_change

# print(revenue)
# print(profit_history)
       
print(
    "Financial Anaylsis \n"
    "------------------------------ \n"
    f'Total Months: {months} \n'
    f'Total: {total_sum} \n'
    f'Average Change: {average_change} \n'
    f'Greatest Increase in Profits: {max} \n'
    f'Greatest Decrease in Profits: {min} \n'
    )
