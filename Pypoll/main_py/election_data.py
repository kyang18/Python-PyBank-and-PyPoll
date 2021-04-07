#Create file paths across operating systems and read the csv file
import os
import csv

# Module for reading the csv file 
csvFile = os.path.join('..','resources','election_data.csv')

# Set variables
csvDataset = []
csvDataset_Candidate = []
csvDataset_VoterID = []
summary_votes = []

# Open the Csv
with open(csvFile,'r') as electionFile:
        csvRead = csv.reader(electionFile,delimiter=',')

        #print(csvRead)
        csv_header = next(csvRead)        
        
        #print(f"CSV Header: {csv_header}")
        for row in csvRead:
            csvDataset.append({
            'voterID': row[0], \
            'county': row[1], \
            'candidate': row[2]
            })
            csvDataset_Candidate.append(row[2])             
            csvDataset_VoterID.append(row[0])              

# The total number of votes cast
total_votes = len(csvDataset_VoterID)

# A complete list of candidates who received votes
unique_candidate = []
def unique():
    global unique_candidate     

    for x in csvDataset_Candidate:
       
        # check if candidate exists in the unique list or not
        if x not in unique_candidate:
            unique_candidate.append(x)

unique()

# The percentage of votes each candidate won
# The total number of votes each candidate won
def sumVotes():
    for z in unique_candidate:                      
        votes = 0                                   
         
        for c in csvDataset:                        
            if z == c["candidate"]:                 
                votes += 1  

        #print(votes)
        pctVotes = round(((votes/total_votes) * 100), 3)     
        summary_votes.append({'candidate': z,'pctVotes': pctVotes, 'totalVotes': votes})

#print(summary_votes) 
sumVotes()                                          
                               
# The winner of the election based on popular vote 
winnerChickenDinner = None                          
def winner():
    rockTheVote = 0                                 
    global winnerChickenDinner                     
    for x in summary_votes:                        
        if x['totalVotes'] > rockTheVote:             
            rockTheVote = x['totalVotes']             
            winnerChickenDinner = x['candidate']    

winner()

#Print the analysis
print("Election Results\n")
print("----------------------------\n") 
print(f"Total Votes: {total_votes}\n")
print("----------------------------\n") 
for x in summary_votes:
    print("{0}: {1:.3f}% ({2:.0f})\n".format(x['candidate'], x['pctVotes'], x['totalVotes']))
print("----------------------------\n") 
print(f"Winner: {winnerChickenDinner}\n")
print("----------------------------\n") 

#  Export a text file with the results
output= open("PyPoll.txt", 'w')
output.write("Election Results\n")
output.write("----------------------------\n") 
output.write(f"Total Votes: {total_votes}\n")
output.write("----------------------------\n") 
for x in summary_votes:
    output.write("{0}: {1:.3f}% ({2:.0f})\n".format(x['candidate'], x['pctVotes'], x['totalVotes']))
output.write("----------------------------\n") 
output.write(f"Winner: {winnerChickenDinner}\n")
output.write("----------------------------\n") 