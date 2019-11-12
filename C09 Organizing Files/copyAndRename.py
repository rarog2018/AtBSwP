# My personal script for my personal usage

import re, os, shutil

# function definition
def copyFiles(prefix, extension, source='', destination='', number=0):
	# prefix and extension regex
	nameF = "(" + prefix + ")(\d+)(\D+)(\." + extension + ")"
	nameRegex = re.compile(nameF)
	
	# check if the destination path exists, if not create it
	if not os.path.exists(destination):
		os.makedirs(destination)
		
	# validate the path
	if os.path.exists(source):
		print("The path is valid. Starting search process...")
		
		# check for matches in the folder
		for filename in os.listdir(source):
			
			mo = nameRegex.search(filename)
			
			# check if filename matches
			if mo == None:
				continue
			
			# copy only the files greater or equal to our number
			if int(number) <= int(mo.group(2)):
				
				# get rid of group(3) part of the file name
				newName = mo.group(1) + mo.group(2) + mo.group(4)
				newName = os.path.join(destination, newName)
				filename = os.path.join(source, filename)
				
				print("Copying %s to %s..." % (filename, newName))
				# copy from source to destination with new name
				shutil.copy(filename, newName)
	
	else :
		print("Given path does not exist")
		return False
	

# specify prefix
prefix = input("Type the prefix of the files that you want to copy: ")

# specify what file extension do you want to search for
extension = input("Type the extension of the files that you want to copy: .")

# specify number 
number = input("From which file number: ")

# specify the folder that you want to search
source = input("Type the path to the folder that you want to search:\n")

# specify where to copy the files
destination = input("Type where you want to copy the files: \n")

# function call
copyFiles(prefix, extension, source, destination, number)


