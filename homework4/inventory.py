#!/usr/bin/python2
#ECE 2524 Homework 4 Problem 1 Chinmay Ghotkar

import argparse
import sys
import fileinput

parser = argparse.ArgumentParser(description='This is an inventory database program.')
parser.add_argument('-f', '--data-file', help = 'path to the data file to read at startup')
args = parser.parse_args()
inventory = []

for line in fileinput.input(args.data_file):
	splitLine = line.split()
	inventory.append(dict(PartId=splitLine[0],Description=splitLine[1],Footprint=splitLine[2],Quantity=splitLine[3])

	x = len(inventory)
