import os
import csv

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

# Define function for candidates that received votes, run function to populate list
def unique(pol):
    for i in pol:
        if i not in unique_pol:
            unique_pol.append(i)
unique(pol)

# Count ballots to find total number of votes cast
num_votes = len(ballot)

# Declare values for total number of votes received for each candidate
v1 = pol.count(unique_pol[0])
v2 = pol.count(unique_pol[1])
v3 = pol.count(unique_pol[2])

# Find percentage of the vote received
# Secondary formatted value to truncate decimals
pv1 = (int(v1) / int(num_votes)) * 100
pvf1 = "{:.3f}".format(pv1)
pv2 = (int(v2) / int(num_votes)) * 100
pvf2 = "{:.3f}".format(pv2)
pv3 = (int(v3) / int(num_votes)) * 100
pvf3 = "{:.3f}".format(pv3)

# Dictionary to determine winner
vote_count = {
    unique_pol[0]: v1,
    unique_pol[1]: v2,
    unique_pol[2]: v3
}

# Declaring the winning vote value
winning_vote = max(vote_count.values())

# Loop through dictonary and return winner's name
for key, value in vote_count.items():
    if value == winning_vote:
        winner = key

# Print Results
print(f'Election Results \n'
      f'------------------------------------- \n'
      f'Total Votes Cast: {num_votes} \n'
      f'------------------------------------- \n'
      f'Candidates Receving Votes: \n\n'
      f'{unique_pol[0]}:  {float(pvf1)}%  ({v1}) \n'
      f'{unique_pol[1]}:            {float(pvf2)}%  ({v2})\n'
      f'{unique_pol[2]}:      {float(pvf3)}%  ({v3})\n'
      )
print(f'------------------------------------- \n'
      f'Winner:     {winner}'
      )