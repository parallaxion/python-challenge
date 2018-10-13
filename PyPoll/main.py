import csv
import math

file = open('election_data.csv', mode='r')

#convert to dictionary with csv reader library
#csvdat = csv.DictReader(dat)
csvdat = csv.reader(file)

rowcount = 0
total = 0.0
votes = {}
#no clue why this takes a user programmed loop
for row in csvdat:
    if row[0] == "Voter ID":
        continue
    r1 = int(row[0])
    total = total + r1
    if row[2] in votes:
        votes[row[2]] = votes[row[2]] + 1
    else:
            votes[row[2]] = 1
    

    rowcount += 1
winner = ["", 0]
f = open("results.txt", mode='w')
print("=========================Election Results=============================")
f.write("=========================Election Results=============================\n")
print("Totes Votes: " + str(rowcount))
f.write("Totes Votes: " + str(rowcount)+"\n")
print("-----------------------------------------------------------------------")
f.write("-----------------------------------------------------------------------\n")
for cand in votes:
    print(cand + ": " + str(round((votes[cand] /rowcount)*100, 2)) + "% ("+ str(votes[cand])+ ")")
    f.write(cand + ": " + str(round((votes[cand] /rowcount)*100, 2)) + "% ("+ str(votes[cand])+ ")\n")
#print(votes)
print("------------------------------------------------------------------------")
f.write("------------------------------------------------------------------------\n")
for cand in votes:
    if votes[cand] > winner[1]:
        winner[0] = cand
        winner[1] = votes[cand]
    
print("Winner: " + winner[0])
f.write("Winner: " + winner[0]+"\n")
print("------------------------------------------------------------------------")
f.write("------------------------------------------------------------------------\n")


