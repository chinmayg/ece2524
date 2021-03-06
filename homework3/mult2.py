#!/usr/bin/python2
# ECE 2524 Homework 3 Problem 2 Chinmay Ghotkar
import argparse
import sys
import fileinput

parser = argparse.ArgumentParser(description='Multiplies Number from Standard Input.')
parser.add_argument('files', nargs = '*',  metavar='file', help='reads the file to multiply numbers')
parser.add_argument('--ignore-blank', action='store_true', dest='ignore_blank', help='the program will ignore blank line')
parser.add_argument('--ignore-non-numeric',action='store_true',dest = 'ignore_non_numeric', help='the program will ignore non-numerics')
args = parser.parse_args()
product = 1.0

try:
	for line in fileinput.input(args.files):
		if args.ignore_blank and not args.ignore_non_numeric:
			if line != "\n":
				product = product * float(line)
		elif args.ignore_non_numeric and not args.ignore_blank:
			try:
				product = product * float(line)
			except ValueError:
				product = product
		elif args.ignore_blank and args.ignore_non_numeric:
			if line != "\n":
				try:
					product = product * float(line)
				except:
					product = product
		else:	
			if line == "\n":
				print product
				product = 1.0
			else:
				product = product * float(line)
	print product
except ValueError as e:
    s = str(e)
    sys.stderr.write(s)
    sys.exit(1)
