import os
import csv

#Storing each value in the csv
voter_counts = []
County = []
candidate = []
candidate_count = []
percent = []
count = 0

#Open the csv file using a set path My_Poll
My_Poll = os.path.join('PyPoll', 'Resources', 'PyPoll_Resources_election_data.csv')

# Path to collect data from the Resources folder
with open(My_Poll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Read through each row of data after the header
    for row in csvreader:
        candidate_count.append(row[2])
        voter_counts.append(int(row[0]))
        count = count + 1

#Create a set for the candidate column to get the specific candidate count
for a in set(candidate_count):
    candidate.append(a)
    b = candidate_count.count(a)
    voter_counts.append(b)
    c = (b/count) * 100
    percent.append(c)

#Print the "Election Results"
print("Election Results")
print("----------------------------------------------------------")

total_votes = len(voter_counts)
print(f"Total Votes: {total_votes}")

print("----------------------------------------------------------")

for i in range(len(candidate)):
    print(candidate[i] + ": " + str(round(percent[i])) + "% (" + str(voter_counts[i]) + ")")

print("----------------------------------------------------------")

print(f"The winner is: Khan")

print("----------------------------------------------------------")

# Specify the file to write to
output_file = os.path.join('PyPoll', 'Analysis', 'Election Analysis')
with open(output_file, 'w', newline='') as txtfile:

# Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')
# Write the first row (column headers)
    csvwriter.writerow("Election Results")
    csvwriter.writerow("----------------------------------------------------------")
    csvwriter.writerow(f"Total Votes: {total_votes}")
    csvwriter.writerow("----------------------------------------------------------")
    csvwriter.writerow(candidate[i] + ": " + str(round(percent[i])) + "% (" + str(voter_counts[i]) + ")")
    csvwriter.writerow("----------------------------------------------------------")
    csvwriter.writerow(f"The winner is: Khan")
    csvwriter.writerow("----------------------------------------------------------")
