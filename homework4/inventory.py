#!/usr/bin/python2
#ECE 2524 Homework 4 Problem 1 Chinmay Ghotkar
import ast
import argparse
import sys
import fileinput
import shlex
#This function will parse the commands
def parseTheCommand(command):
	splitLine = shlex.split(command)
	cmdInfo = [];
	cmd = splitLine[0]
	for item in splitLine:
		if item.find('=') != -1:
			cmdInfo.append(item)
		if cmd == 'add':
			if item.find('{') != -1:
				cmdInfo.append(item)
	return (cmd, cmdInfo)	
#This function will read the inputs in the file
def createInventory(fileName,inventory):
	for line in fileinput.input(fileName):
		if line != "":
			splitLine = shlex.split(line)
			tempDict = dict(PartID=splitLine[0],Description=splitLine[1],Footprint=splitLine[2],Quantity=splitLine[3])
			inventory.append(tempDict)
	fileinput.close()
#This function will add a new entry into the inventory
def addToInventory(stringDict,inventory):
	try:
		tempDict = ast.literal_eval(stringDict)
		inventory.append(tempDict)
		print "%%% add item finished %%%\n"
		return (inventory)
	except ValueError as e:
	        s = str(e)
	        sys.stderr.write(s)
    		sys.exit(1)

#This function will remove an entry from the inventory
def removeFromInventory(commandStr,inventory):
	try:
		key,value = commandStr.split('=')
		for item in inventory:
			if item[key] == value:
				inventory.remove(item)
		print "%%% remove item finished %%%\n"
	except KeyError as e:
		s = str(e)
    		sys.stderr.write(s)
    		sys.exit(1)
#This function will print the dictionary
def printDictionary(dictionary):
	keys = ['PartID','Description','Footprint','Quantity']
	output = ""
	for key in keys:
		output = output + str(dictionary[key]) + "\t\t\t"
	print output
#This function will list all of the functions
def listInventory(command,inventory):
	if len(command) == 0:
		for item in inventory:
			printDictionary(item)	
	else:
		try:
			key,value = command[0].split('=')
			printDictionary(inventory[0])
			for item in inventory:
		    		if item[key] == value:
					printDictionary(item)
		except KeyError as e:
			s = str(e)
        	        sys.stderr.write(s)
	                sys.exit(1)
#This function allows the user to change values in the inventory
def changeValuesInventory(command,inventory):
	try:
		keyChange, changeVal = command[0].split('=')
		keyPart,partID = command[1].split('=')
		for item in inventory:
               		if item['PartID'] == partID:
				item[keyChange] = changeVal
		print "%%% change item finished %%%\n"
	except KeyError as e:
		s = str(e)
		sys.stderr.write(s)
		sys.exit(1)
#This function writes to the file
def writeInventoryToFile(fileName,inventory):
	keys = ['PartID','Description','Footprint','Quantity']
	f = open(fileName[0],'w')
	output = ''
	for item in inventory:
		for key in keys:
			output = output + str(item[key]) + "\t\t\t"
		f.write(output +"\n")
		output = ""
	f.close()
#main Method
def main():
	try:
		parser = argparse.ArgumentParser(description='This is an inventory database program.')
		parser.add_argument('-f', '--data-file',help = 'path to the data file to read at startup')
		args = parser.parse_args()
		inventory = []
		createInventory(args.data_file,inventory)
		for line in sys.stdin:
			cmd, cmdInfo = parseTheCommand(line)
			if cmd == 'add':
				addToInventory(cmdInfo[0],inventory)
			elif cmd == 'remove':
				removeFromInventory(cmdInfo[0],inventory)
			elif cmd == 'set':
				changeValuesInventory(cmdInfo,inventory)
			elif cmd == 'list':
				listInventory(cmdInfo,inventory)
			else:
				print "didn't understand command"
		writeInventoryToFile(args.data_file,inventory)
	except IOError as e:
	        s = str(e)
                sys.stderr.write(s)
                sys.exit(1)
	sys.exit(0)
if  __name__ =='__main__':main()

