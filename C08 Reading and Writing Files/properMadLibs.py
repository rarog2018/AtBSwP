# Mad Libs program

''' 1. It should read in text files
		a) maybe simple version will just read file given inside the code
		b) more advanced will read file(s) in current directory
		c) or get a path from the user 
			- if so, it has to validate the path, and only if the path is
			valid, do the next steps
	2. It should store the contents of the file in a list or string
	3. It should search the file for ADJECTIVE, NOUN, ADVERB, or VERB
	4. User should be asked for a replacement word for every single
	occurence of our searched words separately
	5. Save the results in a new text file
	6. Print the results on the screen
	
'''
import re, os

# open the text file
filename = '.\\file.txt'
fileH = open(filename, 'r')

# store the contents of the file in content variable and close the file
content = fileH.read()
fileH.close()

# list to determine usage of 'a' or 'an' article
an = ["ADJECTIVE", "ADVERB"]

# our regular expression 
replaceRegex = re.compile(r"ADJECTIVE|NOUN|VERB|ADVERB")

# findall gives us list of every occurence of our regex in given text
# we loop through this list
for word in replaceRegex.findall(content):
	# maybe this could be done with "A\w*" regex, but i do not see how
	# would it prevent doubling those 2 lines after ':'
	if word in an:
		# store user input in a variable
		toReplace = input("Enter an %s: " % (word.lower()))
		# this usage of sub() is presented in documentation
		content = re.sub(replaceRegex, toReplace, content, 1)
	else:
		toReplace = input("Enter a %s: " % (word.lower()))
		# this usage of sub() is presented in the book
		content = replaceRegex.sub(toReplace, content, 1)
		
# store results in a file with prefix
newFileH = open('new' + os.path.basename(filename), 'w')
newFileH.write(content)

# print results	
print(content)
