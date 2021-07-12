#Import CSV Data File
import os
import csv

#Path to collect data from the Resources folder
#def create_file(budget_data_csv):
path_file = os.path.join('\\Users\\stephaniewilson2014\\Documents\\steph\\Butler Education\\Homework\\Python Homework\\PyPoll\\Resources\\election_data.csv')
candidates = 0
total_votes = 0
list_candidates= []
candidate_winner = 0
candidate_name = ""

#Open and read csv file
with open(path_file) as data:
    reader = csv.reader(data)
    header = next(reader)
    first_row=next(reader)
    first_value=int(first_row[0])
    #print row
    for row in reader:
        #print(row)
        #total votes cast
        total_votes+=1 
    #print(total_votes)
        #list of candidates who received votes
        candidates=row[2]
        #print(candidates)
        if candidates in list_candidates:
            list_candidates[candidates] += 1
            #print(candidates)
    #print(list_candidates)
        #else:    
            #list_candidates[candidates] =1
           

    #compute percentage and candidate votes
        percentage_votes = (candidates/total_votes)*100
        print(percentage_votes)

    #total number of votes
        total_votes_candidate = (list_candidates[candidates]/total_votes)
        print(total_votes_candidate)

    #winner
        candidate_winner=max(list_candidates)

    results = (f"Financial Analysis\n"
f"----------------------"
f"Total Votes: {total_votes}\n"
f"Candidates: {candidates}\n"
f"Percentage Votes: ${candidates/total_votes}*100\n"
f"Total Votes Candidate: {total_votes_candidate}\n"
f"Winner: {candidate_winner}\n")

print(results)

write_results = os.path.join('\\Users\\stephaniewilson2014\\Documents\\steph\\Butler Education\\Homework\\Python Homework\\PyPoll\\Analysis\\analysis.text')
with open(write_results, 'w+') as textfile:
        textfile.write(str(results)) 