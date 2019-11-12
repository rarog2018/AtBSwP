# formats how the list is printed
def format_print(given_list):
	string = ''
	lngth = len(given_list)
	i = 1
	for el in given_list:
		if i < lngth - 1:
			string += str(el) + '. '
		elif i < lngth:
			string += str(el)
		else:
			string += ' and ' + str(el)
		i += 1
	return string

spam = ['bananas', 'apples', 'tofu', 'cats']
print(format_print(spam))

bacon = [3.14, 'cat', 11, 'cat', True]
print(format_print(bacon))
