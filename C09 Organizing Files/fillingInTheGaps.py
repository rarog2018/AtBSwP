# Write a program that finds all files with a given prefix, such as 
# spam001.txt, spam002.txt, and so on, in a single folder and locates 
# any gaps in the numbering (such as if there is a spam001.txt and 
# spam003.txt but no spam002.txt).
# Have the program rename all the later files to close this gap.

# Create regex that will have 3 groups - prefix, number and extension
# Find only the files that exactly match the given prefix 
# Standardize how the number is represented in a name 
# Set count to 1 and go through the list

import os, re, shutil

def renameF(path, oldName, newName):
	print("Renaming %s to %s..." % (oldName, newName))
	
	# store absolute paths in name variables
	newName = os.path.join(pathF, newName)
	oldName = os.path.join(pathF, oldName)
	
	# rename
	shutil.move(oldName, newName)

while True:
	pathF = input("Type a folder that you want to search through:\n")
	if os.path.exists(pathF):
		break

# specify the prefix
prefix = input("Type the prefix: ")

# create the regex pattern
prefixString = "(" + prefix + ")" + "(\d+)(\.\w*)" 
prefixRegex = re.compile(prefixString)

# store valid filenames in this list
fileList = []

# search for matches in given folder and standardize the number format
print("Standardizing filename format: ")
for filename in os.listdir(pathF):
	
	# check if filename meets our requirements and store it in variable
	mo = prefixRegex.search(filename)
	
	# if match object is empty then proceed the next file
	if mo == None:
		continue
	
	# check if the file already has good format, if not
	if mo.group(2) != mo.group(2).zfill(3):
		# create new formatted name that will have number represented  
		# with 3 digits, this will help with sorting
		newName = mo.group(1) + str(mo.group(2)).zfill(3) + mo.group(3)
		# add formatted name to the list
		fileList.append(newName)
	
		# function for less repetition
		renameF(pathF, filename, newName)
	# if format is good then just append unchanged filename to the list
	else:
		fileList.append(filename)

# set count to 1
count = 1
print()
# go through sorted list of files that matched the regex pattern
for filename in sorted(fileList):
	
	mo = prefixRegex.search(filename)
	
	# check if the currently proceeded file has required number
	if count == int(mo.group(2)):
		count += 1
		# if it has then proceed next file
		continue
	
	# if not create new name with count as a number
	newName = mo.group(1) + str(count).zfill(3) + mo.group(3)
	count += 1
	
	renameF(pathF, filename, newName)
	

