# import csv and read
import os
import csv

pybank_path = os.path.join('Resources','budget_data.csv')

csvfile = open(pybank_path)

csvreader = csv.reader(csvfile, delimiter=',')

# read header row first
csv_header = next(csvreader)
# print(f'CSV Header: {csv_header}')

# take data from two columns: date and profit/losses
# store date and profit/losses in containers
date = []
profit_losses = []

# iterate through each row
# and append to new lists


for row in csvreader:
    date.append(row[0])
    profit_losses.append(row[1])

# zip together into a single tuple
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
#print('Total months: ' + str(total_months))


# calculate net total of profits/losses over entire period
for each_month in pybank_list:
    #print(each_month[1])
    current_finances = int(each_month[1])
    net_total += current_finances
    # print(net_total)
    # exit()

# calculate changes in profit/losses over entire period, then find average of those changes
    if previous_finances != 0:
        
        value_change = current_finances - previous_finances
        cum_value_change += value_change
        row_index += 1
        # print(f'Value change is {value_change}')

    previous_finances = current_finances
    # find average of changes
    average_change = round((cum_value_change / (total_months - 1)), 2)
    
    # greatest increase in profits (date and amount) over entire period
    if value_change > profit_increase:
        profit_increase = value_change
        #need to pull value from each_month[0]
        profit_increase_date = each_month[0]

    # greatest decrease in losses (date and amount) over entire period
    if value_change < profit_decrease:
        profit_decrease = value_change
        profit_decrease_date = each_month[0]

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
