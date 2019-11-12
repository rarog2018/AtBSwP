# debugged the program
import random

guess = ''
# added a tuple to use 'toss' variable as an index
glst = ('tails', 'heads')
# moved tuple from while statement to a variable
while guess not in glst:
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
# changed the condition
if glst[toss] == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	# fixed typo
	guess = input()
	toss = random.randint(0, 1)
	# again, changed condition
	if glst[toss] == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
