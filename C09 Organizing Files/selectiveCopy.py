# Program that walks through a folder tree and searches for files with
# a certain file extension (such as .pdf or .jpg). Copy these files from 
# whatever location they are in to a new folder.

import re, os, shutil

# function definition
def copyFiles(extension, source='', destination=''):
	# i am using regex instead of endswith function for practice purposes
	ext = '.*\.' + extension + '$'
	extensionRegex = re.compile(ext)
	
	# check if the destination path exists, if not create it
	if not os.path.exists(destination):
		os.makedirs(destination)
		
	# validate the path
	if os.path.exists(source):
		print("The path is valid. Starting search process...")
		
		# walk through the directory tree
		for foldername, subfolders, filenames in os.walk(source):
			print("The current folder: " + foldername)
			for filename in filenames:
				# check if filename has our extension
				if extensionRegex.search(filename):
					# just for visual clarity 
					print("Copying " + filename)
					# merge dirname with basename to get absolute path
					shutil.copy(foldername + '\\' + filename, destination)
	else :
		print("Given path does not exist")
		return False
	
	
# specify what file extension do you want to search for
extension = input("Type the extension of the files that you want to copy: .")

# specify the folder that you want to search
source = input("Type the path to the folder that you want to search:\n")

# specify where to copy the files
destination = input("Type where you want to copy the files: \n")

# function call
copyFiles(extension, source, destination)

