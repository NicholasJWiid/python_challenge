# Import necessary modules
import os
import csv

#  Set csv path, open csv file, skip header row, and save data in a list
csvpath = os.path.join(".", "Resources", "election_data.csv")
with open(csvpath, 'r') as csvfile:
    election_csv = csv.reader(csvfile, delimiter=',')
    next(election_csv, None)
    election_data = [item for item in election_csv]

# Calculate total number of votes counted
total_votes = len(election_data)

# Create a sorted list of unique candidates
candidate_list = sorted([candidate for candidate in set([candidate[2] for candidate in election_data])])

# Set initial variable values
votes_won = {}
candidate_votes = 0
highest_votes = 0
winner = ""

# Loop through each candidate in the candidate list and look for name matches in election_data, count total votes for each candidate, save candidate name and vote count into a dictionary
for candidate in candidate_list:
    for row in election_data:
        if row[2] == candidate:
            candidate_votes += 1
    votes_won[candidate] = candidate_votes
    if candidate_votes > highest_votes:
        highest_votes = candidate_votes
        winner = candidate
    candidate_votes = 0

# Save results to a variable in the correct print format, looping through dictionary values
results = f'\nElection Results\n\n----------------------------\n\n'f'Total Votes: {total_votes}\n\n----------------------------\n\n' + '\n'.join([f"{key}: {value/total_votes*100:0.3f}% ({value})\n"for key, value in votes_won.items()]) + f'\n\n----------------------------\n\nWinner: {winner}\n'
print(results)

# Write results to txt file
textpath = os.path.join('.', 'Analysis', 'results.txt')
with open(textpath, 'w') as resultsfile:
    resultsfile.write(results)