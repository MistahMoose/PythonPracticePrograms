

#Creating the game board
def PrintGameboard(Grid):
	print('  |' + '0' + ' | ' + '1' + ' | ' + '2')
	print('0 |' + ' ' + Grid[0][0] + ' | ' + Grid[0][1] + ' | ' + Grid[0][2])
	print('1 |' + ' ' + Grid[1][0] + ' | ' + Grid[1][1] + ' | ' + Grid[1][2])
	print('2 |' + ' ' + Grid[2][0] + ' | ' + Grid[2][1] + ' | ' + Grid[2][2])

def PlayerMove(Grid,PlayerToken):  #Asks player for move, Checks space isn't already occupied
		print('Player ' + PlayerToken + " Please make your move! \n \nEnter the Row of your move: ")
		PlayerMoveRow = int(input())
		print('Player ' + PlayerToken + " Enter the Column of your move: ")
		PlayerMoveColumn = int(input())

		while(Grid[PlayerMoveRow][PlayerMoveColumn] != '_'):#Check if space is free
			print('This space is already occupied! Please re-enter your move!')
			print('Player ' + PlayerToken + " Please make your move! \n \nEnter the Row of your move: ")
			PlayerMoveRow = int(input())
			print('Player ' + PlayerToken + " Enter the Column of your move: ")
			PlayerMoveColumn = int(input())

		Grid[PlayerMoveRow][PlayerMoveColumn] = PlayerToken


		

#Compares players move to grid to check if they won.
def CheckForWin(Grid, PlayerToken):

	print('Checking for win..')
	#python prints columns then rows, Unlike C++ Which is rows then columns.
	if(Grid[0][0] == PlayerToken and Grid[1][0] == PlayerToken and Grid[2][0] == PlayerToken):#First column
		print('Player '+ PlayerToken + ' Wins!')
		return True
	elif(Grid[0][1] == PlayerToken and Grid[1][1] == PlayerToken and Grid[2][1] == PlayerToken):#Second Column
		print('Player '+ PlayerToken + ' Wins!')
		return True
	elif(Grid[0][2] == PlayerToken and Grid[1][2] == PlayerToken and Grid[2][2] == PlayerToken):#Third Column
		print('Player '+ PlayerToken + ' Wins!')
		return True
	elif(Grid[0][0] == PlayerToken and Grid[0][1] == PlayerToken and Grid[0][2] == PlayerToken):#Top Row
		print('Player '+ PlayerToken + ' Wins!')
		return True
	elif(Grid[1][0] == PlayerToken and Grid[1][1] == PlayerToken and Grid[1][2] == PlayerToken):#Middle Row
		print('Player '+ PlayerToken + ' Wins!')
		return True
	elif(Grid[2][0] == PlayerToken and Grid[2][1] == PlayerToken and Grid[2][2] == PlayerToken):#Bottom Row
		print('Player '+ PlayerToken + ' Wins!')
		return True
	elif(Grid[0][0] == PlayerToken and Grid[1][1] == PlayerToken and Grid[2][2] == PlayerToken):#Diagonal top left to bottom right
		print('Player '+ PlayerToken + ' Wins!')
		return True
	elif(Grid[2][0] == PlayerToken and Grid[1][1] == PlayerToken and Grid[0][2] == PlayerToken):#diagonal top right to bottom left
		print('Player '+ PlayerToken + ' Wins!')
		return True
	

	for i in range(len(Grid)):
		for j in range(len(Grid[i])):
			if Grid[i][j] == '_':
				return False
	return True



#Runs the game for Player vs player, input done manually.
def GameMode_Player_Vs_Player(Grid):
	print('Begin!\n')
	print('Player 1 makes the first move! \nPlease enter the grid location you would like to place a token! \n')
	PrintGameboard(Grid)
	Turns = 0 #iterator
	PlayerX = 'X'
	PlayerO = "O"
	PlayerToken = PlayerX
	GameOver = False
	while(Turns < 10):

		PlayerMove(Grid, PlayerToken)

		GameOver = CheckForWin(Grid, PlayerToken)
		PrintGameboard(Grid)
		if(GameOver == True ):
			break
		elif(PlayerToken == PlayerX):#At end of turn change token to other player
			PlayerToken = PlayerO
		elif(PlayerToken == PlayerO):
			PlayerToken = PlayerX


#Initialize the board
Grid = [['_']*3 for Tiles in(range(3))] #This method creates a new object per loop 
# Grid = [['_']*3]*3 <-This method copies the grid by reference



print('Welcome to TicTacToe! \n To play versus another player, Enter 1. \n To exit Enter 3.')

UserInput = int(input())
print('\n')

if(UserInput == 1):
	#begin play
	print("You've chosen to play against another player! Player 1 will be X, Player 2 Will be O! \n")
	GameMode_Player_Vs_Player(Grid)
elif(UserInput == 3):
	#Exit program
	print('Exiting..')
else:
	print("I'm sorry, that isn't an option. \n To play versus another player, Enter 1. \n To play versus a computer, Enter 2.")

#ask player if they want to play against human or computer
#enter game loop for human vs human

#enter game loop for human vs ai