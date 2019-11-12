# Program that walks through a folder tree and searches for exceptionally
# large files or folders, ones that have a file size of more than 100MB.
# Prints these files with their absolute path to the screen.

import os

while True:
	pathF = input("Type a folder that you want to search through:\n")
	if os.path.exists(pathF):
		break

# calculate bits
ourSize = 100 * 1048576

# empty dictionary that will contain paths as keys and filesizes in mb
# as values
hashF = {}

# walk through folder tree
for foldername, subfolders, filenames in os.walk(pathF):
	
	# go though each file
	for filename in filenames:
		# create absolute path to a given file
		currPath = os.path.join(foldername, filename)
		# store the size of current file in a variable
		current = os.path.getsize(currPath)
		# if the size is greater than 100 mb
		if  current > ourSize:
			# add it to our dictionary with the size as a value
			hashF[currPath] = round((current / 1048576), 2)
			# os.unlink(currPath)			better not uncomment this
	
# print the results
for k,v in hashF.items():
	print(k + ": " + str(v) + " mb")
