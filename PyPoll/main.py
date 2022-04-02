import os
import csv

from pyrsistent import v

csvpath = os.path.join('Resources', 'election_data.csv')

ballot = []
county = []
pol = []
unique_pol = []

with open(csvpath) as csvfile:
# Declares how the csv file should be read
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for col in csvreader:
        ballot.append(col[0])
        county.append(col[1]) 
        pol.append(col[2])

def unique(pol):
    for i in pol:
        if i not in unique_pol:
            unique_pol.append(i)

num_votes = len(ballot)
unique(pol)

v1 = pol.count("Charles Casper Stockham")
v2 = pol.count("Diana DeGette")
v3 = pol.count("Raymon Anthony Doane")

pv1 = (int(v1) / int(num_votes)) * 100
pvf1 = "{:.3f}".format(pv1)
pv2 = (int(v2) / int(num_votes)) * 100
pvf2 = "{:.3f}".format(pv2)
pv3 = (int(v3) / int(num_votes)) * 100
pvf3 = "{:.3f}".format(pv3)

print(f'Election Results \n'
      f'------------------------------------- \n'
      f'Total Votes Cast: {num_votes} \n'
      f'Candidates Receving Votes: \n\n'
      f'{unique_pol[0]}:  {float(pvf1)}%  ({v1}) \n'
      f'{unique_pol[1]}:            {float(pvf2)}%  ({v2})\n'
      f'{unique_pol[2]}:      {float(pvf3)}%  ({v3})\n'
      )
print(f'------------------------------------- \n'
      f'Winner:'
      )