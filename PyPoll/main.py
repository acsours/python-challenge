# import csv file
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv') 

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    for each_row in csvreader:
        print(each_row)

        exit()

# calculate total number votes cast
# calculate complete list candidates who received votes
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