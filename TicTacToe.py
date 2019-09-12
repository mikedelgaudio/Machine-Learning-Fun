
#Tic Tac Toe Game

#functions: main, weclome playGame
#response couldve been in its own function!!!

debug = True

def main():
    """Main function for the game"""
    welcome()
    while True:
        if debug: print("About to enter playGame()")
        playGame()
        response = input("Would you like to play again? (y or n): ").strip()#get rid of the end of the spaces w strip this important it wouldve been "y\n" which we dont want
        if not response in ["y","Y", "yes", "Yes", "Yup", "si", "oui", "youbetcha"]:#could be in its own func
            print("Bye!")
            return

def welcome():
    """Prints welcome message, we could put rules for the game and any other info the user might need to know"""
    print("Welcome to tic-tac-toe!")

def playGame():
    """Play one game of ticTacToe"""
    if debug: print("Entering the playGame() function")
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
    """Takes the board and the current player(1 or 2) as input. Asks the player for their move. If it's a legit move,
    the change is made to the board. Otherwise, the player is asked again until a valid move is provided"""
    print("Player " + str(player) + "\'s turn")
    while True:
        row = int(input("Enter the row: ").strip())
        column = int(input("Enter the column: ").strip())
        if row < 0 or row > 2 or column < 0 or column > 2:
            print("That\'s not a valid location on the board! Try again.")
        elif board[row][column] != " ":
            print("That cell is already taken, try again!")
        else:
            board[row][column] = str(player)
            break

def printBoard(board):
    if debug: print("Entering the printBoard() function")
    for row in range(0,3):
        print(" ", end = "")
        for column in range(0, 3):
            print(board[row][column], end = " ")
            if column < 2: print("|", end = " ")
        print() #Causes a LineBreak!
        if row < 2: print("-" * 11)


def boardFull(board): #checking the prop of 2D array... we are checking if a slot is empty... check all rows and columns that an entry is not blank
    if debug: print("Entering the boardFull() function")
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True


def getWinner(board):
    if debug: print("Entering getWinner() function")
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

#if __name__ == "__main__":
#    main()

print(main())

