import csv
import os

file_path = os.path.join("election_data.csv")
 
with open(file_path,"r",newline="") as file_handle:
    csvreader = csv.reader(file_handle, delimiter = ",")
 
# boilerplate code for reading a csv file
 
    header = next(csvreader, None) # None is case sensitive; header is removed from the iterator object cvsreader
    vote = 0 # total number of votes cast
    candidate_to_vote = {}

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
   
    for row in csvreader:
       # print(row)
        vote = vote + 1
        candidate = row[2]
        if candidate not in candidate_to_vote:
            candidate_to_vote[candidate] = 0
        candidate_to_vote[row[2]] = candidate_to_vote[row[2]] + 1

    print("total num of vote",vote)
    print("--------------------")
    
    max = 0
    winner = ""
    i = 0
    percent_vote = []

    for can, num_of_vote in candidate_to_vote.items():
        percentage = int(num_of_vote/vote*100)
        percent_vote.append(percentage)
        print(f"Candiate:{can}; Number of votes:{num_of_vote} ({percent_vote[i]}%)")
        i=i+1
        
        if num_of_vote > max:
            max = num_of_vote
            winner = can
    
    
    print("winner is", winner)
    print(len(candidate_to_vote))
    print(candidate_to_vote)


