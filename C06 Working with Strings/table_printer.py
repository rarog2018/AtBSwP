#Table printer

def printTable(lst):
	"""Prints given list as a formatted table"""
	#store max length of each column 
	colWidth = [0] * len(lst)
	for i in range(len(lst)):
		colWidth[i] = get_max(lst[i])
		
	#print the table
	for i in range(len(lst[i])):
		for j in range(len(lst)):
			print(lst[j][i].rjust(colWidth[j]) + ' ', end='')
		print()
		
def get_max(lst):
	max_ln = 0
	for i in lst:
		if(len(i) > max_ln):
			max_ln = len(i)
		else:
			continue
	return max_ln
	
tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]
			 
printTable(tableData)
