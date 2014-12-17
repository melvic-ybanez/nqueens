'''
Created on Dec 14, 2014

@author: melvic
'''

import sys

        
def has_row_threats(board, col):
    predicate = lambda i: i != col and board[col] == board[i]
    return has_threats(board, col, predicate)

def has_diagonal_threats(board, col):
    predicate = lambda i: abs(i - col) == abs(board[i] - board[col]) != 0
    return has_threats(board, col, predicate)

def has_threats(board, col, predicate):
    for i in range(col):
        if predicate(i):
            return True
    return False

def generate_solutions(board_size):        
    board = [0]
    size = lambda: len(board)

    while True:     
        if board[-1] > board_size - 1:
            if size() == 1:
                return
            del board[-1]
            board[-1] += 1
        elif has_row_threats(board, size() - 1) or has_diagonal_threats(board, size() - 1):
            board[-1] += 1
        elif size() == board_size:
            yield board
            board[-1] += 1
        else:
            board.append(0)              
            

if __name__ == '__main__':
    def get_board_size():
        board_size = raw_input('Enter the size of the board:')
        try:
            return int(board_size)
        except ValueError:
            pass
        
    board_size = get_board_size()
    if not board_size:
        print 'Invalid board size'
        sys.exit()
    solutions = generate_solutions(board_size)
    
    count = 0
    for solution in solutions:
        print solution
        count += 1
    print 'Total number of distinct solutions:', count
        
