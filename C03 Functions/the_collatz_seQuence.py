# The simplest impossible math problem

def collatz(num):
	if number % 2 == 0:
		print(int(number / 2))
		return number / 2
	else:
		print(int(3 * number + 1))
		return 3 * number + 1

while True:
	try:		
		number = int(input("Enter number: "))
	except ValueError:
		print("Please enter and integer.")
	else:
		while number != 1:
			number = collatz(number)
		break
