# ECE 2524 HW1 Problem 2 Chinmay Ghotkar

print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
with open('account', 'r') as f:
    # or read it line by line
    for line in f:
	if 'Blacksburg' in line:
		line.rstrip('\n')
		splitLine = line.split()
		newLine = [splitLine[4],splitLine[1],splitLine[0],splitLine[2]]
		print ', '.join(newLine)
