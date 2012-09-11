#ECE 2524 Homework 2 Problem 1 Chinmay Ghotkar
import sys
if len(sys.argv) == 2:
	with open(sys.argv[1], 'r') as f:
		for line in f:       #reading line by line
			splitLine = line.split(':')
			print splitLine[0].rstrip('\n'),'\t',splitLine[6].rstrip('\n')
else:
	print "Please enter only the path to the file"
