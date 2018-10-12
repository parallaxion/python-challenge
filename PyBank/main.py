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
avrage = 0
low = 0
hig = 0.0
#no clue why this takes a user programmed loop
for row in csvdat:
    if row[0] == "Date":
        continue
    r1 = int(row[1])
    total = total + r1
    if r1 < low:
        low = r1
    if r1 > hig:
        hig = r1
    #saved for later?
    csvdict[rowcount] = row

    rowcount += 1
lenc = len(csvdict)
print("=========================Financial Analysis=============================")
print("Total Months: " + str(lenc))
print("Total: " + str(total))
print("Average: " + str(total/lenc))
print("Biggest Profit: " + str(hig))
print("Biggest Loss: " + str(low))
print("------------------------------------------------------------------------")


