import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Defining lists to store values
date = []
revenue = []

# Open csv file
with open(csvpath) as csvfile:
    
    # Define sum_revenue to add up values of revenue list
    def sum_revenue(csvreader):
        total = 0
        for row in csvreader:
            total = int(total) + int(row)
        return total
    
    # Declares how the csv file should be read
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # for loop to add values of date and revenue
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
        # count number of months in months list
        months = len(date)
        
print(f'The amount of months present is {months} and the sum of revenue is {sum_revenue(revenue)}')
        
    # print(months)
    # print(profit)
        
        

