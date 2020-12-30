# import csv file
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv') 


# declare some variables
vote_count = 0
vote_percentage = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0
popular_vote = 0
candidate = ""

# create a dictionary to hold candidate names
candidate_list = {}

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')



    for each_row in csvreader:
        # calculate total number votes cast
        vote_count += 1
        candidate = each_row[2]
        # calculate complete list of candidates who received votes
        # check value at each_row[2]
        if candidate == "Khan":
            khan_vote += 1
        if candidate == "Correy":
            correy_vote += 1
        if candidate == "Li":
            li_vote += 1
        if candidate == "O'Tooley":
            otooley_vote += 1
    

    khan_percentage = (khan_vote/vote_count)*100
    correy_percentage = (correy_vote/vote_count)*100
    li_percentage = (li_vote/vote_count)*100
    otooley_percentage = (otooley_vote/vote_count)*100
    
    output = f"""
    Election Results
    -------------------------------
    Total Votes: {vote_count}
    -------------------------------
    Khan: {khan_percentage:.3f}% ({khan_vote})
    Correy: {correy_percentage:.3f}% ({correy_vote})
    Li: {li_percentage:.3f}% ({li_vote})
    O'Tooley: {otooley_percentage:.3f}% ({otooley_vote})
    """
    
    print(output)
    
    # print(f'Khan total votes: {khan_vote}')
    # print(f'Correy total votes: {correy_vote}')
    # print(f'Li total votes: {li_vote}')
    # print(f"O'Tooley total votes: {otooley_vote}")
    # # print(f'{candidate}')          
    # print(f'Total votes: {vote_count} ')  

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