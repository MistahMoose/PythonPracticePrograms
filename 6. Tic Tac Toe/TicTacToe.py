

#Creating the game board
def PrintGameboard(Grid):#TODO: Print grid numbers and layou
	print(' ' + Grid[0][0] + ' | ' + Grid[1][0] + ' | ' + Grid[2][0])
	print(' ' + Grid[0][1] + ' | ' + Grid[1][1] + ' | ' + Grid[2][1])
	print(' ' + Grid[0][2] + ' | ' + Grid[1][2] + ' | ' + Grid[2][2])

#Function for the AI's turn TODO: Create AI actions, Place tokens in logical way / Prevent player from winning
def ComputerMove():

	print('something heere')


#Compares players move to grid to check if they won.
def CheckForWin(Grid, PlayerToken):

	print('put list of win conditions')
	#python prints columns then rows, Unlike C++ Which is rows then columns.
	if(Grid[0][0] == PlayerToken and Grid[1][0] == PlayerToken and Grid[2][0] == PlayerToken):#top cross
		print('something here')
	elif(Grid[0][1] == PlayerToken and Grid[1][1] == PlayerToken and Grid[2][1] == PlayerToken):#middle cross
		print('something here')
	elif(Grid[0][2] == PlayerToken and Grid[1][2] == PlayerToken and Grid[2][2] == PlayerToken):#Bottom cross
		print('something here')
	elif(Grid[0][0] == PlayerToken and Grid[0][1] == PlayerToken and Grid[0][2] == PlayerToken):#First column
		print('something here')
	elif(Grid[1][0] == PlayerToken and Grid[1][1] == PlayerToken and Grid[1][2] == PlayerToken):#second column
		print('something here')
	elif(Grid[2][0] == PlayerToken and Grid[2][1] == PlayerToken and Grid[2][2] == PlayerToken):#Third column
		print('something here')
	elif(Grid[0][0] == PlayerToken and Grid[1][1] == PlayerToken and Grid[2][2] == PlayerToken):#Diagonal top left to bottom right
		print('something here')
	elif(Grid[2][0] == PlayerToken and Grid[1][1] == PlayerToken and Grid[0][2] == PlayerToken):#diagonal top right to bottom left
		print('something here')
#Runs the game for Player vs player, input done manually.
def GameMode_Player_Vs_Player():
	print('Begin!')
	print('Player 1 makes the first move! \n Please enter the grid location you would like to place a token!')

	UserInput = input()

	#Execute turns and moves, print gameboard at beginning of each turn
	#


#Initialize the board
Grid = [['_']*3 for Tiles in(range(3))] #This method creates a new object per loop 
# Grid = [['_']*3]*3 <-This method copies the grid by reference

Grid[2][0] = 'x'
Grid[1][1] = 'x'
Grid[0][2] = 'x'
PrintGameboard(Grid)


print('Welcome to TicTacToe! \n To play versus another player, Enter 1. \n To play versus a computer, Enter 2.')

UserInput = int(input())

if(UserInput == 1):
	#begin play
	print("You've chosen to play against another player! Player 1 will be X, Player 2 Will be O!")
elif(UserInput == 2):
	#begin computer play
	print('something heere')
elif(UserInput == 3):
	#Exit program
	print('something heere')
else:
	print("I'm sorry, that isn't an option. \n To play versus another player, Enter 1. \n To play versus a computer, Enter 2.")

#ask player if they want to play against human or computer
#enter game loop for human vs human

#enter game loop for human vs ai