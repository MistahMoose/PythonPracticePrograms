#! python3

#The "shebang" line above tells windows what to compile the program with

print('What grade did you receive in class?')
try:
	classGrade = int(input()) #input is received as string, converted with int() statement
#sublimetext does not support input, testing this program is impossible without using a CMD or Sublime text addon

#python doesn't have inherit switch statements, Will substitute with else if

	if classGrade >= 0 and classGrade <= 59:
		print('You received an F!')
	elif classGrade >= 60 and classGrade <= 69:
		print('You received a D!')
	elif classGrade >= 70 and classGrade <= 79:
		print('You received a C!')
	elif classGrade >= 80 and classGrade <= 89:
		print('You received a B!')
	elif classGrade >= 90 and classGrade < 100:
		print('You received an A!')
	elif classGrade == 100:
		print('You received a perfect Score!')
	elif classGrade < 0 or classGrade> 100:
		print('Invalid input, Impossible grade!') #Wanted to use Try Except for input validation of grades between 0-100
		#however giving a number larger than the cases isn't "invalid"
except:
	print('invalid input, Please retry.')
#When running this program using cmd, You will need to have quotes "" around the file path if the path has spaces in it.
#For example
#py.exe "D:\Programming\Python Practice Programs\1. Grading Program\Grading Program.py"
#Is the execution line for this python program.

#Will use batchfiles in the future for more complicated programs

#Python project 1, Finished!