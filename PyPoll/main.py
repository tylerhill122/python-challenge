import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

ballot = []
county = []
pol = []

with open(csvpath) as csvfile:
# Declares how the csv file should be read
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for col in csvreader:
        ballot.append(col[0])
        county.append(col[1]) 
        pol.append(col[2])
    
