#! python3


i = 5
print('Please Enter Any Number except 5') #Can only concatenate strings, convert i into string
userInput = int(input())
while i != userInput:
	i = userInput #change i to previous user input
	print('Please Enter Any Number except ' + str(i)) #Can only concatenate strings, convert i into string
	userInput = int(input())


print("Hey you weren't supposed to enter " + str(i) + "!!!" )