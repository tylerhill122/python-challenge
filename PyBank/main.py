import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

date = []
profit = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
        months = len(date)
    print(months)
        
        

