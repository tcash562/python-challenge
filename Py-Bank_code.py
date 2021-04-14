
import os
import csv

MyBank = os.path.join('Pybank','Resources','budget_data.csv')

#Storing each value in csv in an empty list
date = []
profit_losses = []
monthly_changes = []
monthly_changes_average = []
total = []
total_months = []
increase_date = []

# Define the function
with open(MyBank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit_losses.append(int(row[1]))

# Print out the header "Financial Analysis"
print("Financial Analysis")
print("---------------------")

# Print out the total months
total_months = len(date)
print(f"Total Months:{total_months}")

# Print the sum of the Profit losses
total = sum(profit_losses)
print(f"Total: ${total}")

# Monthly changes can be found by adding the profit losses and than by the number of items
monthly_changes = sum(profit_losses)/len(profit_losses)
print(f"Average Change: ${monthly_changes}")

#Retrieving Max and Min dates
date = max(date)
date = min(date)

#Max profit losses
greatest_increase_profits = max(profit_losses)
print("Greatest Increase in Profits: " + str(date) + " ($" + str(greatest_increase_profits) + ")")

#Min profit losses
greatest_decrease_profits = min(profit_losses)
print("Greatest Decrease in Profits: " + str(date)  + " ($" + str(greatest_decrease_profits)+ ")")

print("----------------------------------------------------------")

# Specify the file to write to
output_file = os.path.join('Pybank', 'Analysis', 'Financial Analysis')
with open(output_file, 'w', newline='') as txtfile:

# Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')
# Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
# Write the second row
    csvwriter.writerow(f"Total Months:{total_months}")
    csvwriter.writerow(f"Total: ${total}")
    csvwriter.writerow(f"Average Change: ${monthly_changes}")
    csvwriter.writerow("Greatest Increase in Profits: " + str(date) + " ($" + str(greatest_increase_profits) + ")")
    csvwriter.writerow("Greatest Decrease in Profits: " + str(date)  + " ($" + str(greatest_decrease_profits)+ ")")
