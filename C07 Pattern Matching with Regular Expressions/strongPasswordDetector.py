# Program checks if the password is strong
#import regular expression module
import re
''' 1.It should ask user to type the password
	2.It should check if the password has at least 8 characters
	3.It should check if there is an uppercase letter
	4.It should check if there is an lowercase letter
	5.It should check if there is a digit
	6.It should print the result '''
	
def isStrong(text):
	print("\nRunning tests:")
	#check if there are at least 8 characters
	lengthRegex = re.compile(r'\w{8,}')
	if lengthRegex.search(text) == None:
		print("Test 1 failed")
		return False
	print("Test 1 passed")
	#check if there is at least 1 lower case letter
	lowerCaseRegex = re.compile(r'[a-z]+')
	if lowerCaseRegex.search(text) == None:
		print("Test 2 failed")
		return False
	print("Test 2 passed")
	#check if there is at least 1 upper case letter
	upperCaseRegex = re.compile(r'[A-Z]+')
	if upperCaseRegex.search(text) == None:
		print("Test 3 failed")
		return False
	print("Test 3 passed")
	#check if there is at least 1 digit
	digitRegex = re.compile(r'[0-9]+')
	if digitRegex.search(text) == None:
		print("Test 4 failed")
		return False
	print("Test 4 passed\nYour password is strong!")
	return True

# Ask user to type password and store it in passw variable
while True:
	passw = input("Please type your password: (type q to quit) ")
	if passw == 'q':
		break
	isStrong(passw)
