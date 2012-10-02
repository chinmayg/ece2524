#!/usr/bin/python2
#ECE 2524 Homework 4 Problem 1 Chinmay Ghotkar

import argparse
import sys
import fileinput
import shlex

#This will read the inputs in the file
def createInventory(fileName,inventory):
	for line in fileinput.input(fileName):
		splitLine = shlex.split(line)
		tempDict = dict(PartId=splitLine[0],Description=splitLine[1],Footprint=splitLine[2],Quantity=splitLine[3])
		inventory.append(tempDict)
	return (inventory)
#Main Method
def main():
	parser = argparse.ArgumentParser(description='This is an inventory database program.')
	parser.add_argument('-f', '--data-file', help = 'path to the data file to read at startup')
	args = parser.parse_args()
	inventory = []
	createInventory(args.data_file,inventory)
	print len(inventory)

if  __name__ =='__main__':main()
	
