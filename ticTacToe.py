import sys

def icon(playerNumber):
    """
    returns 'O' or 'X' if input playerNumber 1 or 2, otherwise returns a blank space string.
    """
    if playerNumber == 1:
        return 'O'
    elif playerNumber == 2:
        return 'X'
    else:
        return ' '

def showBoard(gameState):
    """
    prints the board in its current gameState.
    """
    print('')
    for row in gameState:
        print([icon(square) for square in row])

def swapTurn(playerNumber):
    """
    flip player turn between 1 and 2.
    """
    if playerNumber == 1:
        return 2
    elif playerNumber == 2:
        return 1

def checkWin(game, w):
    """
    for given game state 'game' and player 'w'. returns True if player 'w' has won, or False if not.
    """
    win = False
    if game[0] == [w, w, w] or game[1] == [w, w, w] or game[2] == [w, w, w]:
        win = True
    elif game[0][0] == w and game[1][0] == w and game[2][0] == w:
        win = True
    elif game[0][1] == w and game[1][1] == w and game[2][1] == w:
        win = True
    elif game[0][2] == w and game[1][2] == w and game[2][2] == w:
        win = True
    elif game[0][0] == w and game[1][1] == w and game[2][2] == w:
        win = True
    elif game[0][2] == w and game[1][1] == w and game[2][0] == w:
        win = True
    return win

def turnCycle(playerNumber, gameState):
    try:
        move = input('player {} ({}),  make your move [row, col]: '.format(playerNumber, icon(playerNumber))).strip()
        if move.lower() == 'quit':
            sys.exit()
        move = move.split(',')
        if len(move) != 2:
            raise ValueError
        move = [int(coord) - 1 for coord in move]
        if gameState[move[0]][move[1]] == ' ':
            gameState[move[0]][move[1]] = playerNumber
        else:
            print('illegal move. please try another sqaure.')
    except ValueError:
        print('\nerror. please enter your move with the correct format:')
        print('row, column')
        print('for example to mark the top right square,  enter: 1, 3\n')

def main():
    print('***********************')
    print('welcome to Tic Tac Toe!')
    print('***********************')
    print('in turns please enter your desired move coordinates in the following format:')
    print('row, column')
    print('for example to mark the top right square,  enter: 1, 3\n')

    # initial conditions:
    stateState = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    startingPlayer = 1

    whosTurn = startingPlayer
    gameState = [list(row) for row in stateState]
    gameOn = True

    while gameOn:
        turnCycle(whosTurn, gameState)
        showBoard(gameState)
        if checkWin(gameState, whosTurn):
            gameOn = False
            print('************************')
            print('game over! player {} won!'.format(whosTurn))
            print('************************')
        whosTurn = swapTurn(whosTurn)

        fullSquares = 0
        for square in gameState[0] + gameState[1] + gameState[2]:
            if square != ' ':
                fullSquares += 1
        if fullSquares == 9 and gameOn:
            gameOn = False
            print('*************************')
            print('game over! it\'s a draw...')
            print('*************************')

        if not gameOn:
            yn = input('do you want to play another game [type Y for yes or anything else to quit]?\n')
            if yn.lower() == 'y':
                gameState = [list(row) for row in stateState]
                gameOn = True
            else:
                sys.exit()

if __name__ == '__main__':
    main()

