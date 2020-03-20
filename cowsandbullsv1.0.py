#Cows and Bulls version 1.1
#Made for python3

from random import randint


#create a list with the four random digits as strings to be guessed
def getguessing():
	random_integer = randint(0, 9999)
	if 1000 <= random_integer <= 9999:
		hidden_string = str(random_integer)
	elif 100 <= random_integer <= 999:
		hidden_string = '0' + str(random_integer)
	elif 10 <= random_integer <= 99:
		hidden_string = '00' + str(random_integer)
	else:
		hidden_string = '000' + str(random_integer)
	return hidden_string

#function created to separate compare pattern list from its source
def patternrefresher(integer_string):
	hidden_list = []
	for t in integer_string:
		hidden_list.append(t)
	#print(hidden_list) #debug
	return hidden_list

#define a function that returns a user guess as a list of 4 digits as string each with a valid input
def getguess():
	rawinput = input('Enter four digits: ')
	if len(rawinput) == 4 and rawinput.isdigit():
		input_list = []
		for digit in rawinput:
			input_list.append(digit)
		#print(input_list) #debug
		return input_list
	else:
		print('Invalid input.\n\nTry again...')
		return False
		
		

#define a function that checks if guess matches guessing number, returning True or False
def guesscheck(pattern, attempt):
	if pattern == attempt:
		print("Congratulations! You've guessed it right!")
		return True
	else:
		print('Not a match.')
		return False

#define a function that counts cows and bulls, printing and returning their count
def cowsbulls(pattern, attempt):
	
	#function variables
	pattern
	attempt
	cows = 0
	bulls = 0
	count0 = 0
	count1 = 0
	count2 = 0
	
	
	#count cows and remove them from lists
	for x in attempt:
		if x == pattern[count0]:
			cows += 1
			pattern[count0] = 'a'
			attempt[count0] = 'a'
			pass
		else:
			pass
		count0 += 1
	#print(f'guess: {attempt}\nguessed: {pattern} -- after cow count') #debug
	
	#count bulls while removing counted ones
	for y in attempt:
		if y == 'a':
			continue
		else:
			for z in pattern:
				if z == y:
					bulls += 1
					pattern[count2] = 'a'
					attempt[count1] = 'a'
					count2 = 0
					break
				else:
					count2 += 1
					continue
			count1 += 1
			count2 = 0
			continue
				
		count1 += 1
	#print(f'attempt: {attempt}\npattern: {pattern} -- after bull count') #debug
	
	#end the function by printing the results and returning cows and bulls count
	print(f'Cows: {cows}, Bulls: {bulls}\n\nTry again...')
	return (cows, bulls)
	
	

#game start
print(
'''===================================
Welcome to the Cows and Bulls Game!
===================================

Cows and bulls is a simple and brief
guessing game in which you have to
guess a randomly generated number of
four digits (0000 to 9999).

But don't worry! It won't be that hard!
Firstly, you'll have unlimited attempts to
correctly guess it. Also, you'll get some
clues allong the process.

If your guess is not entirely correct, but
get some numbers right, you'll earn cows
and bulls for each correct digit of your
answer.

Cows and bulls both represent right
number guessings, but the different
between them is that the cows also
represent right numbers guessings
at the right places, while bulls are right
numbers, but at wrong places.

Knowing your cows and bulls on each
attempt, you'll be one step closer into
unveilling the secret number.

Good luck and enjoy!!

[If you're not seeing the entire instructions
on this page, please scroll up.]

This is your secret number for this time:
 >>>>>>[ ? ? ? ? ]<<<<<<
Wondering which one it might be?
Place a GUESS!!
''')

#get hidden pattern to match only once per run
guess_string = getguessing()

#create game loop
loops_count = 0
not_match = True
while not_match:
	
	#count game loops
	loops_count += 1
	
	#get user guess and refresh pattern
	hidden = patternrefresher(guess_string)
	bet = getguess()
	
	#check input
	if not bet:
		continue
	
	#check if guess is correct
	if guesscheck(hidden, bet):
		not_match = False
	
	#if not, then count and print cows and bulls and restart game loop
	else:
		cowsbulls(hidden, bet)

print(f'You won the game in {loops_count} tries.')
