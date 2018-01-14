#!/usr/bin/env python
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys


# Count # of pieces in given row
def count_on_row(board, row):
    return sum(board[row])


# Count # of pieces in given column
def count_on_col(board, col):
    return sum([row[col] for row in board])


#Count no of pieces in diagonals
#forward downward
def count_on_diagonal(board,r,c):
    diagonal_list=[]
    x=r+1
    y=c+1
    if (r!=N-1 or c!=N-1):
        while (x<N and y<N):
            diagonal_list.append(board[x][y])
            #print diagonal_list
            x+= 1
            y+= 1
    return sum(diagonal_list)
#forward upwards
def diagonal2(board,r,c):
    diagonallist2=[]
    x = r - 1
    y = c + 1
    #print ('rc')
    #print r, c
    if (r != 0 or c != N - 1):
        #print('x,y',x,y)
        while (x>=0 and y<N):
            diagonallist2.append(board[x][y])
            #print('diagonal2')
            #print diagonallist2
            x-= 1
            y+= 1
    return sum(diagonallist2)
#backward upward
def diagonal3(board,r,c):
    diagonallist3=[]
    x = r-1
    y = c-1
    if (r!= 0 or c!= 0):
        while (x>=0 and y>=0):
            diagonallist3.append(board[x][y])
            #print diagonallist3
            x-= 1
            y-= 1
    return sum(diagonallist3)

#backward downward
def diagonal4(board,r,c):
    diagonallist4=[]
    x = r+1
    y = c-1
    if (r!= N-1 or c!= 0):
        while(x<N and y>=0):
            diagonallist4.append(board[x][y])
            #print diagonallist4
            x+= 1
            y-= 1
    return sum(diagonallist4)

def diagonal_count(board,r,c):
   count = [ count_on_diagonal(board,r,c),diagonal2(board,r,c),diagonal3(board,r,c),diagonal4(board,r,c)]
   #print('c')
   #print sum(count)
   return sum(count)


# Count total # of pieces on board
def count_pieces(board):
    return sum([sum(row) for row in board])


# Return a string with the board rendered in a human-friendly format for queens
def printable_board(board):
    #print board[a-1]
    return "\n".join([" ".join(["Q" if col==1 else "X" if (col=='a') else "_" for col in row]) for row in board])


# Return a string with the board rendered in a human-friendly format for rooks
def printable_board1(board):
    return "\n".join([" ".join(["R" if col == 1 else "X" if (col == 'a') else "_" for col in row]) for row in board])


# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1, ] + board[row][col + 1:]] + board[row + 1:]


# Get list of successors of given board state for n-queens
def successors(board):
    cand=[]
    for r in range(0,N):
        for c in range(0,N):
            if count_pieces(board)<N and count_on_row(board,r)<1 and count_on_col(board,c)<1 and diagonal_count(board,r,c)<1 and not(r==a-1 and c==b-1):
                #print[add_piece(board,r,c)]
                cand+=[ add_piece(board, r, c) ]
    return cand


# Get list of successors of given board state for n-rooks
def successors2(board):
    for r in range(0, N):
        for c in range(0, N):
            if count_pieces(board) < N and count_on_row(board, r) < 1 and \
                            count_on_col(board, c) < 1 and not(r==a-1 and c==b-1):
                return [add_piece(board, r, c)]


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
           all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
           all([count_on_col(board, c) <= 1 for c in range(0, N)])


cache = []


# Solve n-queens!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe)>0:
        #print('fringe')
        #print fringe
        for s in successors(fringe.pop()):
            if s not in cache:
                cache.append(s)
                #print ('s')
                #print(s)
                if is_goal(s):
                    return(s)
                fringe.append(s)
    return False


# Solve n-rooks!
#start_time=time.clock()
def solve1(initial_board):
    fringe = [initial_board]
    while len(fringe)>0:
        for s in successors2(fringe.pop()):
            #if s not in fringe:
                if is_goal(s):
                    return(s)
                fringe.append(s)
    return False

# This is N, the size of the board. It is passed through command line arguments.
strategy = sys.argv[1]
N = int(sys.argv[2])
a= int(sys.argv[3])
b= int(sys.argv[4])

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0] * N] * N
if strategy=='nqueen':
    print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
    solution = solve(initial_board)
    #print(solution)
    solution[a-1][b-1]= 'a'
    print (printable_board(solution) if solution else "Sorry, no solution found. :(")


if strategy=='nrook':
    print ("Starting from initial board:\n" + printable_board1(initial_board) + "\n\nLooking for solution...\n")
    solution = solve1(initial_board)
    solution[a - 1][b - 1] = 'a'
    print (printable_board1(solution) if solution else "Sorry, no solution found. :(")



