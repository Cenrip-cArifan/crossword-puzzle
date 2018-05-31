#File:        proj2.py
#Author:      Gabriel Kilungya
#Date:        05/09/16
#Lab Section: 15
#UMBC email:  kilgab1@umbc.edu
#Description: Python Word Search file. In this Python file, I will import in a 
#	      word search file and append it to a 2D grid which contains hidden words.
#	      I will also import in a word list file and append it to a list. These
#	      words may appear in the word search: horizontally, vertically, or diagonally
#	      The word search puzzle will be of any size but will always be rectangular
#	      There can be n number of words in the list but there'll always be at least
#	      one word.
#	      For the output: If the word doesn't appear in the puzzle, display it for the 
#	      the sake of the user. If the word does appear in the puzzle, the starting coordinates
#	      should be shown and the direction the word is going in
#	      Directions are: Diagonally(up & left), Up, Diagonally(up & right), Backwards(left)
#			      Right, Diagonally(down & left), Down, and Diagonally(down & right)



#The gridBoard function takes in no parameters. 
#Input: It takes in a word search grid file inputted by the user and opens it up to be read
#	1st For Loop: This for loop, reads in every line of the word search file that was imported
#		      Appends each line on a new line but strips the whitespaces for the sake of
#		      correct indexing when we attain the starting coordinates of the words
#		      The word search file is appended to an empty list called "board"
#	2nd Outer For Loop: This for loop ranges the rows from 0 to length n of the board,
#	3rd Inner For Loop: This for loop ranges the columns of the rows from 0 to length n of the board
#			    Then it prints the board[i][j]; row by column as a matrix grid
#Important to close of a File immediately for the sake of not corrupting data
#Output: Prints the board and Returns the board

def gridBoard():

	puzzleFile = input("What is the puzzle file you would like to import?: ")

	boardFile = open(puzzleFile, "r")

	board = []

	for eachLine in boardFile:

		board.append(eachLine.strip().split())

	for i in range(0, len(board)):

		for j in range(0, len(board[i])):

			print (board[i][j]),

		print

	boardFile.close()

	return board


#The wordList function takes in no parameters.
#Input: It takes in a word list file inputted by the user and opens it up to be read
#	For Loop: This for loop read in each word and strips of whitespaces, then appends
#		  the list of words into an empty list called "words"
#Important to close again all Files that are not in use any more, to not corrupt data
#Output: Prints the words in a list format and returns the words

def wordList():

	listFile = input("What is the word list file you would like to import?: ")
	
	wordFile = open(listFile, "r")

	words = []

	for eachWord in wordFile:

		words.append(eachWord.strip())

	print(words)

	wordFile.close()
	
	return words

#The firstLetterCheck function takes in 4 parameters: the word, the board, the row(i), the column(j), and directions in i & j
#Base Case: The base case checks to see if the length of a word is 0, then it always returns True
#Bounds Check: For row(i) and column(j), if i or j is less than 0 or i or j is greater than length of board,
#	       return False. This is to ensure that when the recursive case checks in every possible direction
#	       There'll be no wrap around but stops at the border of the board and checks in another direction
#Recurisve Case: If the first letter of the board equals a letter found in a location on the board,
#		 First I'll initialize the check of the remain letters of the word to variable "restOfWord"
#		 then return the function itself, with restOfWord as the new conditional check,
#		 also return the row(i) & column(j) but add/subtracted to direction of i & j
#		 direction of i & j are numbers but for the sake of doing it in one recursive function,
#		 these values: -1, 0, 1, will be used in another function
#Output: Returns True or False or the Recursive function depending on satisfied/unsatisfied conditions

def firstLetterCheck(word, board, i, j, i_direction, j_direction):

	if (len(word) == 0):

		return True

	if (i < 0 or i > len(board) - 1):

		return False

	if (j < 0 or j > len(board[i]) - 1):

		return False

	if (word[0] == board[i][j]):

		restOfWord = word[1:]

		return firstLetterCheck(restOfWord, board, i + i_direction, j + j_direction, i_direction, j_direction)

	return False


#The checkWord function takes in 3 parameters: the word, the board, and the directionLabels
#Input: 1st Outer For Loop: This for loop ranges the rows from 0 to length n of the board
#	2nd Inner For Loop: This for loop ranges the columns of the rows from 0 to length n of the board
#	3rd Inner For Loop: This for loop takes in x values & y values, which are integers that determine the direction we will
#			    the remaining letters of a word (word[1:], from firstLetter function) Since 8 diff, we have 3 values for
#			    i & j, because the pair cooridantes.
#	If statement: If the firsLetterCheck function is True, I will create a variable "keyLocation" that will format the 
#		      directions:  Diagonally(up & left), Up, Diagonally(up & right), Backwards(left), Right, Diagonally(down & left),
#		      Down, and Diagonally(down & right); according to their specific x & y coordinates
#		      I will then use the dictionary get(key, Default = " ") method to return the values of the keys(x & y); values(directions)
#Output: If True, then it returns True, the label(value of the keys), and the coordinates i & j(row & col). Otherwise, exit all the nested for loops
#	 Return False, and None for the label and the coordinates i & j

def checkWord(word, board, directionLabels):

	x_value = [-1, 0, 1]
	y_value = [-1, 0, 1]

	for i in range(0, len(board)):

		for j in range(0, len(board[i])):

			for x_direction in x_value:

				for y_direction in y_value:

					if firstLetterCheck(word, board, i, j, y_direction, x_direction):

						keyLocation = '{y}{x}'.format(y=y_direction, x=x_direction)

						label = directionLabels.get(keyLocation, "Not defined direction")

						return True, label, i, j
	else:
		return False, None, None, None

#The main function takes no parameters and is where the other functions will be called and the Python script is executed
#Input: Calls in the gridBoard & wordList functions and respectively assigns them to variables "board" and "words"
#	The variable "directionLabels" is initialized to a dictionary that has keys as x_direction & y_direction that are used in the 
#	firsLetterCheck & wordCheck functions that determine the direction the remaining letters of a word is being searched in.
#	The values of those keys are the kind of direction, the letter is being searched it (The keys are unique, therefore the values must
#	be unique as well)
#	For Loop: This for loop check for every word in words
#		  If/Else statements: If word is found in the board. Print the word, it's starting coordinates(i & j), 
#		  		      it's direction(determined by x_direction & y_direction as we saw earlier and values in dictionaryLabels are returned from
#		  		      variable "labels"
#				      Otherwise, print "The word doesn't appear in the puzzle"
#Output: Print the game header and what the user will be importing. Print "the word, it's starting coordinates and direction it goes", if it is in the board
#	 Print "The word doesn't appear in the puzzle", if it isn't in the board

def main():

	print("Welcome to the Word Search")

	print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")

	board = gridBoard()

	words = wordList()

	directionLabels = {'-1-1': 'diagonally up & left', '-10': 'up', '-11': 'diagonally up & right',

				'11': 'diagonally down & right', '10': 'down', '1-1': 'diagonally down & left',

				'0-1': 'backwards left', '01': 'right'}
				 

	for word in words:
	    found, label, i, j = checkWord(word, board, directionLabels)
	    if found:
	        print("The word", word, "starts in", i,",", j, "and goes", label)
	    else:
	        print("The word", word, "doesn't appears in the puzzle")
	   
    

main()
