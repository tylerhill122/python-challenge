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
# populate profit_history list, tracking change by month over time
for i in range(len(revenue) - 1):
    change = int(revenue[i+1]) + (0 - int(revenue[i]))
    profit_history.append(change)

endtime = (len(revenue)) - 1
months = len(date)

#calculate total change
change = int(revenue[int(endtime)]) - int(revenue[0])
total_change = change / endtime
#format response to 2 decimal
total_change_f = "{:.2f}".format(total_change)

#greatest increase and decrease and total sum
min = min(profit_history)
max = max(profit_history)
total_sum = sum_revenue(revenue)

#finding the dates corresponding to the greatest increase / decrease
for i in range(len(profit_history)-1):
    if profit_history[i] == min:
        min_date = date[i+1]
    elif profit_history[i] == max:
        max_date = date[i+1]
       
print(
    "------------------------------ \n"
    "Financial Anaylsis \n"
    "------------------------------ \n"
    f'Total Months: {months} \n'
    f'Total: ${total_sum} \n'
    f'Average Change: ${total_change_f} \n'
    f'Greatest Increase in Profits: {max_date} (${max}) \n'
    f'Greatest Decrease in Profits: {min_date} (${min}) \n'
    )