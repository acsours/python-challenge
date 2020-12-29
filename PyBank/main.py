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

# print(f'date is {date[0]} and profit/losses is {profit_losses[0]}')
# print(profit_losses[0])
#print(f'{len(date)}{len(profit_losses)}')

# zip together into a single tuple
pybank_list = list(zip(date, profit_losses))

print(pybank_list[11])
# print(date)

# declare variables
net_total = 0
previous_finances = 0
value_change = 0
cum_value_change = 0
row_index = 0

# total number of months in dataset (len)
total_months = len(date)
#print('Total months: ' + str(total_months))
print(f'Total months: {total_months}')  

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
    

print(f'Net total: {net_total} dollars')
print(f'total value change: {cum_value_change}')
print(f'average change is: {average_change}')    



# print(value_change({profits_losses}))
    # go through each month's profit/loss value - profit_losses[1]-profit_losses[0]
    # calculate average 
# greatest increase in profits (date and amount) over entire period
# greatest decrease in losses (date and amount) over entire period
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''
# print analysis to terminal and export text file with results
# write to new file here: where does this need to happen? before or after calculations? I think it happens after...- directions just say export text file with results