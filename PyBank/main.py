# Import necessary modules
import os
import csv

#  Set csv path, open csv file, skip and save header row, and save data in a list
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_csv, None)
    budget_data = [item for item in budget_csv]

# Set initial variable values
month_count = 0
net_total = 0
previous_month = None
total_change = 0
change_counter = 0
greatest_incr = 0
greatest_decr = 0

# Loop through each item in the data
for row in budget_data:
    # Count total number of rows containing data (excluding header row) and calculate net total Profit/Loss
    month_count += 1
    net_total += int(row[1])

    # Calculate cumulative change over the whole period
    current_month = int(row[1])
    if previous_month is not None:
        change = current_month - previous_month
        total_change += change
        change_counter += 1
        
        # Calculate greatest change increase and decrease
        if change > greatest_incr:
            greatest_incr = change
            date_incr = row[0]
        elif change < greatest_decr:
            greatest_decr = change
            date_decr = row[0]
    
    previous_month = current_month

# Calculate average change
pnl_average = round(total_change/change_counter,2)

# Save results to a variable in the correct print format
results = f'\nFinancial Analysis\n\n----------------------------\n\nTotal Months: {month_count}\n\nTotal: ${net_total}\n\nAverage Change: ${pnl_average}\n\nGreatest Increase in Profits: {date_incr} (${greatest_incr})\n\nGreatest Decrease in Profits: {date_decr} (${greatest_decr})\n'

# Print results to the terminal
print(results)

# Write results to txt file
textpath = os.path.join('.', 'Analysis', 'results.txt')
with open(textpath, 'w') as resultsfile:
    resultsfile.write(results)


