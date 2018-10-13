import math
import csv

#open as standard file 
dat = open('budget_data.csv', mode='r')
#convert to dictionary with csv reader library
#csvdat = csv.DictReader(dat)
csvdat = csv.reader(dat)
csvdict = {}
rowcount = 0
total = 0.0
change = 0
avrage = 0
low = 0
hig = 0.0
#no clue why this takes a user programmed loop
for row in csvdat:
    if row[0] == "Date":
        continue
    r1 = int(row[1])
    total = total + r1
    change = change + abs(r1)
    if r1 < low:
        
        low = r1
    if r1 > hig:
        hig = r1
    #saved for later?
    csvdict[rowcount] = row

    rowcount += 1
lenc = len(csvdict)
f = open("results.txt", "w")
print("=========================Financial Analysis=============================")
f.write("=========================Financial Analysis=============================\n")
print("Total Months: " + str(lenc))
f.write("Total Months: " + str(lenc)+"\n")
print("Total: " + str(total)+"\n")
f.write("Total: " + str(total)+"\n")
print("Average Change +/-: " + str(change/lenc)+"\n")
f.write("Average Change +/-: " + str(change/lenc)+"\n")
print("Biggest Profit: " + str(hig))
f.write("Biggest Profit: " + str(hig)+"\n")
print("Biggest Loss: " + str(low))
f.write("Biggest Loss: " + str(low)+"\n")
print("------------------------------------------------------------------------")
f.write("------------------------------------------------------------------------\n")



