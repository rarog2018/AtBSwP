# Write a program that opens all .txt files in a folder and searches for 
# any line that matches a user-supplied regular expression. The results 
# should be printed to the screen.

import os, re

def search_ex(regex):
	# Stores filenames of cwd in a list 
	files = os.listdir('.')
	# Stores our Regex pattern object that matches strings wit txt ext
	textRegex = re.compile(r'.*\.txt$')
	# Empty list to store only files with txt extension, we could approach
	# it in other way - pop nontxt files from 'files' list
	textList = []
	# We go through each string in files list
	for fil in files:
		# Stores Match object in curr variable
		curr = textRegex.search(fil)
		# If the fil string had no .txt extension then curr will be empty
		if curr:
			# If it was not empty then append filename string from MO
			textList.append(curr.group())
	# We have our list, so now we will search through each file in the list
	for fil in textList:
		print("Processing " + fil + " : ")
		# Open the file in read mode
		fileH = open(fil, 'r')
		# We will check if we can find users regex in each line
		for line in fileH:
			# We just want to print the line so we will use search with
			# two parameters
			if re.search(regex, line):
				# If regex is found then print the line 
				print(line.rstrip())
		fileH.close()
		print()

while True:
	regex = input("Please type your regular expression: (type q to quit)\n")
	if regex == 'q':
		break
	search_ex(regex)
