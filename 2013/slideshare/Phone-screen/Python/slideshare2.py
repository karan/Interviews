#!/usr/bin/env python

# simple tetris implementation

board = [['' for i in range(20)] for j in range(10)]

def find_top_row(board, column_num, piece):
    last_row = piece[len(piece) - 1]
    number_of_cols = len(last_row)
    traling_blank = 0
    leading_blank = 0
    
    if last_row[0] == '' and last_row[-1] == '':
        # both (L shaped)
        pass
    elif last_row[0] == '':
        # starts with a blank block
        pass
    elif last_row[-1] == '':
        # ends with blank block
        pass
    
    for i in range(number_of_cols):
        if last_row[i] == '':
            traling_blank += 1
        if last_row[-(i + 1)] == '':
            leading_blank += 1
            
    for row in range(len(board)):
        for col in range(number_of_cols):
            if board[row][column_num + col] != "":
                return row - 1
    return len(board) - 1

def drop_piece(piece, column_num):
    # piece is [][], column_num is int (0-based)
    top_row = find_top_row(board, column_num, piece)
    for row in range(len(piece)):
        for i in range(len(piece[len(piece) - 1])):
            board[top_row - row][column_num + i] = piece[row][i]

def print_board():
    print '*' * 42
    for i in range(len(board)):
        print '|',
        for j in range(len(board[0])):
            print '.' if board[i][j] == "" else board[i][j], 
        print '|'
        print
    print '*' * 42

print_board()
drop_piece([['x', 'x'], ['x', 'x']], 3)
print_board()
drop_piece([['x', 'x'], ['x', 'x']], 3)
print_board()
drop_piece([['z', 'z', ''], ['', 'z', 'z']], 1)
print_board()