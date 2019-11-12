# print the given list of list in different way

def print_list_of_lists(given_list):
	for j in range(len(given_list[0])):			#checks how many colums there are: 6 in this case
		for i in range(len(given_list)):		#checks how many rows there areL 9 in this case
			print(given_list[i][j], end='')		#prints 9 elements from each of the 6 rows
		print('')
		

grid = [['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]

print_list_of_lists(grid)
