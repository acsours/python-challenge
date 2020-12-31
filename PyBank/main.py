# import and read csv
import os
import csv

pybank_path = os.path.join('Resources','budget_data.csv')

csvfile = open(pybank_path)

csvreader = csv.reader(csvfile, delimiter=',')

# read header row first
csv_header = next(csvreader)

# create new lists for data from csv, populate lists with values and zip together
date = []
profit_losses = []

for row in csvreader:
    date.append(row[0])
    profit_losses.append(row[1])

pybank_list = list(zip(date, profit_losses))

# declare variables
net_total = 0
previous_finances = 0
value_change = 0
cum_value_change = 0
row_index = 0
profit_increase = 0
profit_decrease = 0
profit_increase_date = ""
profit_decrease_date = ""

# total number of months in dataset (len)
total_months = len(date)


# calculate net total of profits/losses over entire period
for each_month in pybank_list:
    current_finances = int(each_month[1])
    net_total += current_finances
    

# calculate changes in profit/losses over entire period
    if previous_finances != 0:
        
        value_change = current_finances - previous_finances
        cum_value_change += value_change
        row_index += 1

    previous_finances = current_finances
    
    # find average of changes
    average_change = round((cum_value_change / (total_months - 1)), 2)
    
    # greatest increase in profits (date and amount) over entire period
    if value_change > profit_increase:
        profit_increase = value_change
        profit_increase_date = each_month[0]

    # greatest decrease in losses (date and amount) over entire period
    if value_change < profit_decrease:
        profit_decrease = value_change
        profit_decrease_date = each_month[0]

# print analyis results to terminal
output = f"""
Financial Analysis
------------------------------
Total Months: {total_months}
Net Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {profit_increase_date} (${profit_increase})   
Greatest Decrease in Profits: {profit_decrease_date} (${profit_decrease})
"""

print(output)

#export text file with results
output_path = os.path.join('analysis', 'PyBank.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write(output)
