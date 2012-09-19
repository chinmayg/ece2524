#!/usr/bin/python2
# ECE 2524 Homework 3 Problem 1 Chinmay Ghotkar
import argparse
import sys

parser = argparse.ArgumentParser(description='Multiplies Number from Standard Input.')
args = parser.parse_args()
product = 1.0

try:
	for line in iter(sys.stdin.readline,''):
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
