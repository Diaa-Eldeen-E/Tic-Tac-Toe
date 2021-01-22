"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    
    NoOfX = 0
    NoOfO = 0
    for rows in board:
        for element in rows:
            if(element == X):
                NoOfX += 1
            elif(element == O):
                NoOfO += 1
            
    if(NoOfO > NoOfX):
        return X
    elif(NoOfO == NoOfX):
        return O
    else:
        raise Invalidstate


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    PossActions = []
    
    # Find empty positions
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                PossActions.append((i,j))
                
    return PossActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if the action if valid (range from 0 to 2)
    if(action[0] not in range(3) or action[1] not in range(3)):
        raise OutOfRangeInvalidAction
        
    # Check that this poisition is empty
    if(board[action[0]][action[1]] != EMPTY):
        raise NonEmptyPoisitionInvalidAction
    
    x = copy.deepcopy(board)
    x[action[0]][action[1]] = player(x)
    return  x


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    NoOfO_D1, NoOfX_D1, NoOfO_D2, NoOfX_D2 = 0, 0, 0, 0
    
    for i in range(3):
        NoOfX_R, NoOfX_C, NoOfO_R, NoOfO_C = 0, 0, 0, 0
        
        # Count the diagnoals
        if(board[i][i] == O):
                NoOfO_D1 += 1
        elif(board[i][i] == X):
                NoOfX_D1 += 1
                
        if(board[i][2-i] == O):
                NoOfO_D2 += 1
        elif(board[i][2-i] == X):
                NoOfX_D2 += 1        
                
        for j in range(3):
            
            # Count the rows and columns
            if(board[i][j] == O):
                NoOfO_R += 1
            elif(board[i][j] == X):
                NoOfX_R += 1
            
            if(board[j][i] == O):
                NoOfO_C += 1
            elif(board[j][i] == X):
                NoOfX_C += 1  
        
        # Check if a row or column has 3 Os or 3 Xs        
        if(NoOfO_R == 3 or NoOfO_C == 3):
            return O
        elif(NoOfX_R == 3 or NoOfX_C == 3):
            return X
   
    
    # Check if a diagonal has 3 Os or 3 Xs   
    if(NoOfO_D1 == 3 or NoOfO_D2 == 3):
            return O
    elif(NoOfX_D1 == 3 or NoOfX_D2 == 3):
            return X

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if(winner(board) != None):
        return True
    
    # If there isn't an empty position the game is over
    for rows in board:
        for element in rows:
            if(element == EMPTY):
                return False
        
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if(result == X):
        return 1
    elif(result == O):
        return -1
    else:
        return 0
    



def recurseMiniMax(board):
    """
    Returns the minimum or maximum utility value and the corressponding 
    optimal action for the current player on the board.
    """
    # If the game is over return the utility value
    if(terminal(board)):
        return (utility(board), None)
    
    P = player(board)
    
    # If it's O turn then we want to minimize
    if(P == O): 
        
        minVal = 2
        minAction = None 
        
        '''
        Try all possible actions and return the action with the minimum
        utility value
        '''
        for action in actions(board):
            utilVal = recurseMiniMax(result(board,action))[0]
            if(minVal > utilVal):
                minVal = utilVal
                minAction = action
                
        return (minVal, minAction)
        
    # If it's X turn then we want to maximize
    elif(P == X): 
        maxVal = -2
        maxAction = None 
        
        '''
        Try all possible actions and return the action with the minimum
        utility value
        '''
        for action in actions(board):
            utilVal = recurseMiniMax(result(board,action))[0]
            if(maxVal < utilVal):
                maxVal = utilVal
                maxAction = action
                
        return (maxVal, maxAction)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return(recurseMiniMax(board)[1])
