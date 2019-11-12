# Mad Libs program

''' 1. It should read in text files
		a) maybe simple version will just read file given inside the code
		b) more advanced will read file(s) in current directory
		c) or get a path from the user 
			- if so, it has to validate the path, and only if the path is
			valid, do the next steps
	2. It should store the contents of the file in a list or string
	3. It should search the file for ADJECTIVE, NOUN, ADVERB, or VERB
	4. The search will happen in 'real time', so the user will be asked
	for a replacement words while the search happens
	5. Print the results on the screen
	6. Save them in a new text file
'''

# read the text file
filename = '.\\file.txt'
fileH = open(filename, 'r')
contents = fileH.readlines()
fileH.close()
toReplace = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB', 'VERB.']
newcontents = ''
for line in contents:
	for word in line.split():
		if word in toReplace:
			if word[0] == 'A':
				word = input("Enter an " + word.lower() + ":\n")
				newcontents += word + ' '
			else:
				word = input("Enter a " + word.lower() + ":\n")
				newcontents += word + ' '
		else:
			newcontents += word + ' '
	newcontents += '\n'

print(newcontents)
newFile = open('new' + os.path.basename(filename), 'w')
newFile.write(newcontents)
