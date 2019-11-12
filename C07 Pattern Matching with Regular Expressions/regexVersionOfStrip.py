# Program that mimicks strip() method with regular expressions
# import regular expression module
import re

''' 1. Program should ask user to pass a string and what to do with it
	2. One option would be to remove whitespaces from beginning and end 
	of the string
	3. Another option is to pass a characters that the function should
	remove from the string
	4. The result string should be printed at the end
'''

# function has one optional argument
def regexVersionOfStrip(text, characters=''):
	#if the second argument was not passed then just remove whitespaces
	if characters == '':
		oneRegex = re.compile(r'\S.*\S')
		newString = oneRegex.findall(text)
		return newString
	#if there was a second argument then replace the characters
	else:
		chars = '[^' + characters + ']'			#creates a string that contains our regex
		secondRegex = re.compile(chars)			#regex object with our regex
		newstring = secondRegex.findall(text)	#all matches in given string
		nstring = ''							#new string for visual purposes
		for i in range(len(newstring)):
			nstring += newstring[i]
		return nstring							#returns this new string so we can see that it worked

#
while True:
	string = input("Please type your string: (type q to quit)\n")
	if string == 'q':
		break
	question = input("Do you want to remove characters? (type y/n)")
	if question == 'y':
		chars = input("Type the characters below:\n")
		print(regexVersionOfStrip(string, chars))
	else:
		print(regexVersionOfStrip(string))	
