# import csv file
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv') 


# declare variables
vote_count = 0
vote_percentage = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0
popular_winner = ""
candidate = ""

# Read csv file, skip header
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


    for each_row in csvreader:
        
        # calculate total number votes cast and pull candidate value 
        vote_count += 1
        candidate = each_row[2]
    
        # calculate complete list of candidates who received votes
        if candidate == "Khan":
            khan_vote += 1
        if candidate == "Correy":
            correy_vote += 1
        if candidate == "Li":
            li_vote += 1
        if candidate == "O'Tooley":
            otooley_vote += 1
    
    # use candidate vote totals to calculate percentages
    khan_percentage = (khan_vote/vote_count)*100
    correy_percentage = (correy_vote/vote_count)*100
    li_percentage = (li_vote/vote_count)*100
    otooley_percentage = (otooley_vote/vote_count)*100
    
    # Calculate popular vote winner
    if khan_vote > correy_vote and khan_vote > li_vote and khan_vote > otooley_vote:
        popular_winner = "Khan"

    if correy_vote > khan_vote and correy_vote > li_vote and correy_vote > otooley_vote:
        popular_winner = "Correy"

    if li_vote > khan_vote and li_vote > correy_vote and li_vote > otooley_vote:
        popular_winner = "Li"    
    
    if otooley_vote > khan_vote and otooley_vote > li_vote and otooley_vote > correy_vote:
        popular_winner = "O'Tooley"
    

    # print results in terminal
    output = f"""
    Election Results
    -------------------------------
    Total Votes: {vote_count}
    -------------------------------
    Khan: {khan_percentage:.3f}% ({khan_vote})
    Correy: {correy_percentage:.3f}% ({correy_vote})
    Li: {li_percentage:.3f}% ({li_vote})
    O'Tooley: {otooley_percentage:.3f}% ({otooley_vote})
    -------------------------------
    Winner: {popular_winner}
    """
    
    print(output)


# export text file with results
output_path = os.path.join('analysis', 'PyPoll.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write(output)
