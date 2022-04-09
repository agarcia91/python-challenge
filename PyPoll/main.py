import os
import csv

# variables 
candidates = []
vote_count = []
num_vote = 0


 


    # Set the path
election_dataCSV = '/Users/anthonygarcia/Desktop/python-challenge/PyPoll/Resources/election_data.csv'

    # Open CSV File
with open(election_dataCSV) as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip headers
        Row = next(csvReader,None)

        # Loop for votes
        for Row in csvReader:

            
            num_vote = num_vote + 1

            
            candidate = Row[2]

            # Add other votes to total
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_count[candidate_index] = vote_count[candidate_index] + 1
            
            else:
                candidates.append(candidate)
                vote_count.append(1)

# variables 
percent = []
top_vote = vote_count[0]
top_index = 0

# Percent of votes for candidates
for count in range(len(candidates)):
        vote_percent = vote_count[count]/num_vote*100
        percent.append(vote_percent)
        if vote_count[count] > top_vote:
            top_vote = vote_count[count]
            top_index = count
winner = candidates[top_index]

# Round percentage
percent = [round(x,3) for x in percent]



    
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_vote}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percent[count]}% ({vote_count[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# The output path
output_path = '/Users/anthonygarcia/Desktop/python-challenge/PyPoll/analysis/PyPoll_summary.txt'
        
        # Write summary to text 
with open('/Users/anthonygarcia/Desktop/python-challenge/PyPoll/analysis/PyPoll_summary.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------------\n")
    text.write(f"Total Votes: {num_vote}\n")
    for count in range(len(candidates)):
        text.write(f"{candidates[count]}: {percent[count]}% ({vote_count[count]})\n")
    text.write("---------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("---------------------------\n")
    text.close


