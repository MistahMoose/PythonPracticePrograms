import random

print('Enter 1 to guess the number \n Enter 2 to choose the number!')
GameChoice = int(input()) #convert input to int
if (GameChoice == 1):
	print('Please choose a random number between 1 & 100')

	randomNum = random.randint(1 , 100)

	print(str(randomNum))

	Guess = False
	guessCounter = 0
	while Guess == False:
		userGuess = int(input())
		guessCounter = guessCounter+1
		if (userGuess == randomNum):
			Guess = True
		elif (userGuess > randomNum):
			print('Too high!')
		elif (userGuess < randomNum):
			print('Too low!')

	print("You're right it was " + str(randomNum) + "! it took you " + str(guessCounter) + " Tries!")


elif (GameChoice == 2):
		print("Please give me a number between 1 & 100!")
		userNum = int(input())
		Guess = False
		compGuess = random.randint(1, 100)#generate random number for first guess
		maxGuess = 100 #Set max and min, Necessary if first guess is too low or too high.
		minGuess = 1
		guessCounter = 0
		while(Guess == False):
			print ("My guess is... " + str(compGuess) + "!" )
			print("Enter 1 if I was too high, Or 2 if I was too low! and 3 if I guessed the number!")

			highOrLow = int(input())
			guessCounter =guessCounter+1 #Alternatively can use (guessCounter += 1)

			if (highOrLow == 1):
				maxGuess = compGuess
				compGuess = round((minGuess + maxGuess) / 2)#Rounding number to get rid of decimal for clarity
			elif(highOrLow == 2):
				minGuess = compGuess
				compGuess = round((minGuess + maxGuess) / 2)#Take the average to find the middle.
			elif(highOrLow == 3):
				print("I guessed the number in " + str(guessCounter) + " Tries!")
				Guess = True

elif(GameChoice != 1 and GameChoice != 2):
	print('No choice selected! Exiting..')
