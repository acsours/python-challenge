# import csv file
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv') 


# declare some variables
vote_count = 0
vote_percentage = 0
candidate_vote = 0
popular_vote = 0

# create a dictionary to hold candidate names
candidate_list = {}

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')



    for each_row in csvreader:
        # calculate total number votes cast
        vote_count += 1
            
    print(f'Total votes: {vote_count} ') 
        

# calculate complete list of candidates who received votes
    # check value at each_row[2]
    # if value at each_row[2] is different: start a new count
# calculate percentage of votes each candidate won
# calculate total number of votes each candidate won
# winner of election vased on popular vote
# print analysis to terminal in this format:
    # Election Results
    # -------------------------
    # Total Votes: 3521001
    # -------------------------
    # Khan: 63.000% (2218231)
    # Correy: 20.000% (704200)
    # Li: 14.000% (492940)
    # O'Tooley: 3.000% (105630)
    # -------------------------
    # Winner: Khan
    # -------------------------

# export text file with results