#Tic Tac Toe Game
#Michael DelGaudio

#####
# Working on making a machine learning AI to play against the player.
# You can use debug mode below to switch on console statements.
#####

#####
# KNOWN ISSUES:
# Prints NONE to display if game is over.
#####

#from sklearn import tree

debug = True

def main():
    welcome()
    gameContinue = True
    while (gameContinue == True):
        if debug: print("\n About to enter playGame() \n")
        #Begin the game:
        playGame()
        #After the game:
        response = input("Would you like to play again? (y or n): ").strip()
        response = response.upper()
        if (shouldGameContinue(response) == False) : 
           print("Thanks for playing!") 
           gameContinue = False
        #Known issue: Prints None to display if game is over.

def shouldGameContinue(response):
    if debug : print("\n Inside shouldGameContinue() \n")
    if(response != ["Y", "YES"]):
        return False
    else:
        return True

def welcome():
    #Prints welcome message, we could put rules for the game and any other info the user might need to know
    print()
    print("-" * 40)
    print("Welcome to tic-tac-toe!")
    print()
    print("To make moves please use numbers such as 0 through 2 to select positions.")
    print()

def playGame():
    #Play one game of ticTacToe
    if debug: print("\n Entering the playGame() function \n" + "-" * 50)
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 1
    print("The board looks like this:")
    printBoard(board)
    while not gameOver(board): #check to see if the game is over or tie... if so end
        getMove(board, player) #notice that the board arg is an input/output arg 
        if player == 1 : player = 2 #switch the player for turns
        else: player = 1
        print("The board looks like this:")
        printBoard(board)

def gameOver(board):
    """Returns false if the game is NOT over. Otherwise, prints a message indicating which plater
    has won and then returns TRUE indicating that the game is over"""
    if debug: print("Entering the gameOver function")

    winner = getWinner(board)
    if winner == "1":
        print("Player 1 wins!")
        return True
    if winner == "2":
        print("Player 2 wins!")
        return True
    if boardFull(board):
        print("Tie.")
        return True

    return False

def getMove(board, player):
    #Takes the board and the current player(1 or 2) as input. Asks the player for their move. If it's a legit move, the change is made to the board. Otherwise, the player is asked again until a valid move is provided
    print("Player " + str(player) + "\'s turn")
    while True:
        try:
            row = int(input("Enter the row: ").strip())
            column = int(input("Enter the column: ").strip())
            if row < 0 or row > 2 or column < 0 or column > 2:
                print("That\'s not a valid location on the board! Try again.")
            elif board[row][column] != " ":
                print("That cell is already taken, try again!")
            else:
                board[row][column] = str(player)
                break
        except ValueError:
            print("I'm sorry, I don't understand. Please use values 0 through 2 only.")
            continue

def printBoard(board):
    if debug: print("\n Entering the printBoard() function \n")

    for row in range(0,3):
        print(" ", end = "")
        for column in range(0, 3):
            print(board[row][column], end = " ")
            if column < 2: print("|", end = " ")
        print()
        if row < 2: print("-" * 11)


def boardFull(board): 
    #checking the prop of 2D array... we are checking if a slot is empty... check all rows and columns that an entry is not blank
    if debug: print("Entering the boardFull() function")

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

def computerAI():
    if debug: print("\n Inside computerAI() \n")


def getWinner(board):
    if debug: print("\n Inside getWinner() \n")
    #Check rows
    for row in range(3):
        val = board[row][0]
        if val != " ":
            col = 1
            while col < 3:
                if board[row][col] != val:
                    break
                col += 1
            if col == 3:
                return val
    #Check columns
    for col in range(3):
        val=board[0][col]
        if val != ' ':
            row=1
            while row < 3:
                if board [row][col] != val:
                    break
                row += 1
            if row == 3:
                return val
    #Check major diagonal
    val = board[0][0]
    if val != " ":
        index = 1
        while index < 3:
            if board[index][index] != val:
                break
            index += 1
        if index == 3:
            return val
    #Check minor diagonal
    val = board[0][2]
    if val != " ":
        index = 1
        while index < 2:
            if board[index][3- index -1] != val:
                break
            index += 1
        if index == 3:
            return val 
    return " "

print(main())

