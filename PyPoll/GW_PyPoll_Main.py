import os
import csv

TotalVotes = 0
CandidateVote = 0
election = []

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    namelist = []
    Votelist = []
    

    for row in csvreader:
        TotalVotes += 1
        name = str(row[2])
        
        if name not in namelist:
            namelist.append(name)
            Votelist.append(CandidateVote)
            CandidateVote = 1 
        else: 
            CandidateVote += 1

Votelist.append(CandidateVote)# this is for Raymond
perlist1 = Votelist[1]
perlist2 = Votelist[2]
perlist3 = Votelist[3]

VoteNumber = (perlist1) / TotalVotes    
VotePercentage1 = "{:.3%}".format(VoteNumber)
VoteNumber = (perlist2) / TotalVotes    
VotePercentage2 = "{:.3%}".format(VoteNumber)
VoteNumber = (perlist3) / TotalVotes    
VotePercentage3 = "{:.3%}".format(VoteNumber)

output = f"""
Election Results
----------------------------
Total Votes: {TotalVotes}
-------------------------
{namelist[0]}: {VotePercentage1} ({Votelist[1]})
{namelist[1]}: {VotePercentage2} ({Votelist[2]})
{namelist[2]}: {VotePercentage3} ({Votelist[3]})
-------------------------
Winner: {namelist[1]}
-------------------------

"""

print (output)  

with open("analysis/Election_output.txt", "w") as outfile:
    outfile.write(output)    