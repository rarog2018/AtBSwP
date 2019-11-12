# As an added challenge, write another program that can insert gaps
# into numbered files so that a new file can be added.

# Create regex that will have 3 groups - prefix, number and extension
# Ask user for prefix and a number where to put gap
# Check if given prefix is followed by number
# Check if the given count is in range of number list
# If it is insert the gap

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

# specify the number after which gap has to be created
count = int(input("Type the number above which you want to make the gap: "))

# prefix has to be followed by at least one digit
prefixString = "(" + prefix + ")" + "(\d+)(\.\w*)" 
prefixRegex = re.compile(prefixString)

# store valid match objects in this list
moList = []

for filename in os.listdir(pathF):
	
	# check if filename meets our requirements and store it in variable
	mo = prefixRegex.search(filename)
	
	# if match object is empty then proceed the next file
	if mo == None:
		continue
	# if is good, then append filename to the list
	else:
		moList.append(mo)
		
if len(moList) == 0:
	print("No matches found.")
	
else:	
	newMoList = []
	for mo in moList:
		# check if count is in range
		# if count is not higher than current elements index
		if count > int(mo.group(2)):
			# proceed next element
			continue
		# if it is, this is the place to make gap
		else:
			newMoList.append(mo)
	
	if len(newMoList) == 0:
		print("Indexes in the list are lower than the given number.")
		
	else:
		# to avoid overwriting files start from the last element
		for mo in reversed(newMoList):
			#increment current index
			incNum = int(mo.group(2)) + 1
			
			newName = mo.group(1) + str(incNum).zfill(3) + mo.group(3)
			filename = mo.group(1) + mo.group(2) + mo.group(3)
			
			renameF(pathF, filename, newName)
