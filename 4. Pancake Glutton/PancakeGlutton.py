#! python3

#Found out it compiles without shebang, but most likely because I only have one python on my system.

import random #for getting random # of pancakes eaten, saves having to type them in

print('How many people are having pancakes?')

numEaters = int(input())

listEaters = [] #Create empty list

for i in range (numEaters):#iterate over input creating empty list of numEaters size
#For loops in python are more iterating over a sequence, rather than an interator method 
	listEaters.append(i)#append list with data
	listEaters[i] = str(random.randint(1,10))




listPosBig = 0
listPosSmall = 0


for i in range(numEaters):#go through the list
	if listEaters[listPosBig] < listEaters[i]:#largest list position gets stored
		listPosBig = i
	if listEaters[listPosSmall] > listEaters[i]:
		listPosSmall = i

print('Person '+ str(listPosBig) + ' Ate the most pancakes with:' + str(listEaters[listPosBig]) + ' eaten.')

print('Person '+ str(listPosSmall) + ' Ate the least pancakes with:' + str(listEaters[listPosSmall]) + ' eaten.')

#New code below 
#_____________________________________________________________________________________________________________________

outerlist = [] #using outer inner to help my brain sort arrays
for i in range(numEaters):
	innerlist = [] #declare inside forloop, creates new list to append each loop.
	innerlist.append(i) #need to store person and amount eaten 
	innerlist.append(random.randint(1,10))#originaly had str(random.randint(), but list dont have to be string based.
	outerlist.append(innerlist)#append to outerlist


for i in range(numEaters): #only have to bubblesort for the total people in array
	swapped = False #to terminate loop early if bubblesort finishes before loop ends
	for j in range (0, numEaters-1): #Traverse from 0-9 (10 total)
		if outerlist[j][1] > outerlist[j+1][1]:#grab pos of j and compare to j+1
			outerlist[j] , outerlist[j+1] = outerlist[j+1], outerlist[j]
			swapped = True
	if swapped == False:#if nothing swapped, break loop
		break

for i in range(numEaters):#print list in order of who ate the most
	print('Person: ' + str(outerlist[i][0]) + ' ate: ' + str(outerlist[i][1]))


print('Person: ' + str(outerlist[0][1]) + ' ate the least pancakes at: ' + str(outerlist[0][1]) + ' Pancakes')

print('Person: ' + str(outerlist[numEaters-1][0]) + ' ate the most pancakes at: ' + str(outerlist[numEaters-1][1]) + ' Pancakes')