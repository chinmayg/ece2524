# ECE 2524 Homework 2 Problem 3 Chinmay Ghotkar
import sys

count = 0.00
total = 0.00
maxOwed = 0.00
minOwed = 0.00
avgOwed = 0.00
maxOwedPerson = ""
minOwedPerson = ""

if len(sys.argv) == 2:
	with open('account', 'r') as f:
   	 # or read it line by line
    		for line in f:
			line.rstrip('\n')
			splitLine = line.split()
			amount = float(splitLine[2])
			total += amount
			count = count + 1.00
			if amount > maxOwed:
				maxOwed = amount
				maxOwedPerson = splitLine[1]
			if minOwed == 0:
				minOwed = amount
			elif amount < minOwed:
				minOwed = amount
				minOwedPerson = splitLine[1]	
		avgOwed = total / count

	print "ACCOUNT SUMMARY"
	print "Total amount Owed =",total
	print "Average amount Owed =",avgOwed
	print "Maximum amount Owed =",maxOwed,"by",maxOwedPerson
	print "Minimum amount Owed =",minOwed,"by",minOwedPerson
else:
	print "Please enter only the data file"
