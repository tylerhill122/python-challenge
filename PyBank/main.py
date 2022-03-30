import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

date = []
revenue = []



with open(csvpath) as csvfile:
    
    def sum_revenue(csvreader):
        total = 0
        for row in csvreader:
            total = int(total) + int(row)
        return total
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
        months = len(date)
        
print(sum_revenue(revenue))
        
    # print(months)
    # print(profit)
        
        

