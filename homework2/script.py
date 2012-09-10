#ECE 2524 Homework 2 Problem 1 Chinmay Ghotkar

with open('/etc/passwd', 'r') as f:
	for line in f:       #reading line by line
		splitLine = line.split(':')
		print splitLine[0].rstrip('\n'),'\t',splitLine[6].rstrip('\n')
