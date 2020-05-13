# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:23:01 2020

@author: keren or
"""
#In this exercise, 
#we were asked to exercise the game so that victory / loss / tie situations would be identified.
# What I've done here is that there is a possibility that a human can play against a 
#computer or two computers play against each other.
import copy
import alphaBetaPruning
import computer_one
import computer_two

from os import system
VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1


# location_factor = 100
# HUMAN = 1  # Marks the human's cells on the board
# sequence_factor = {2:1,3:4}
# turn_factor = {HUMAN: -10, COMPUTER: 8}
# turn = {HUMAN: COMPUTER, COMPUTER: HUMAN}

rows = 6
columns = 7
#

class game:
    board = []
    size = rows * columns
    playTurn = HUMAN
    # TODO add
    movs = [0]*columns
    col = -1
    row = -1
    # Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''
#
# def print_decoration(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         print(f"result: {result}")
#         return result
#     return wrapper


def create(s):
    # Returns an empty board. The human plays first.
    # create the board
    s.board = []
    for i in range(rows):
        s.board = s.board + [columns * [0]]

    s.playTurn = HUMAN
    s.size = rows * columns
    s.val = 0.00001

    # return [board, 0.00001, playTurn, r*c]     # 0 is TIE










def cpy(s1):
    # construct a parent DataFrame instance
    s2 = game()
    s2.playTurn = s1.playTurn
    s2.size = s1.size
    s2.board = copy.deepcopy(s1.board)
    # print("board ", s2.board)
    return s2












def printState(s):
#    system("cls")
#    Prints the board. The empty cells are printed as numbers = the cells name(for input)
#     If the game ended prints who won.
    for r in range(rows):
        print("\n|", end="")
        # print("\n",len(s[0][0])*" --","\n|",sep="", end="")
        for c in range(columns):
            print_str = " "
            if s.board[r][c] == COMPUTER:
                print_str = "X"
            elif s.board[r][c] == HUMAN:
                print_str = "O"
            if c == s.col and r == s.row-1:
                print_str = f"\033[93m{print_str}\033[0m"
            print(print_str+'|', end="")

    print()

    for i in range(columns):
        # TODO add
        # if i == s.col:
        #     i = f"\033[93m{i}\033[0m"
        print(" ", i, sep="", end="")

    # print()
    # TODO add
    print("\n|", end="")
    for c in range(columns):
        if s.movs[c] == COMPUTER:
            print("O|", end="")
        elif s.movs[c] == HUMAN:
            print("x|", end="")
        else:
            print(" |", end="")
    print()
    for i in range(columns):
        s.movs[i] = 0
    #עד כאן

    val = computer_one.value(s)

    if val == VICTORY:
        print("I won!")
    elif val == LOSS:
        print("You beat me!")
    elif val == TIE:
        print("It's a TIE")







def isFinished(s):
    # Seturns True iff the game ended
    return computer_one.value(s) in [LOSS, VICTORY, TIE] or s.size == 0





def who_won(s):
    optipn = {LOSS:"computer_two", VICTORY:'computer_one', TIE:'tie'}
    score = computer_one.value(s)
    return optipn.get(score,None)





def isHumTurn(s):
    # Returns True iff it is the human's turn to play
    return s.playTurn == HUMAN





def decideWhoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you : ")) == 1:
        s.playTurn = COMPUTER
    else:
        s.playTurn = HUMAN

    return s.playTurn

def decideWhoIsFirst(s,first):
    # The user decides who plays first
    s.playTurn = first




def getNext(s):
    # returns a list of the next states of s
    ns = []
    for c in list(range(columns)):
        # print("c=", c)
        if s.board[0][c] == 0:
            # print("possible move ", c)
            tmp = cpy(s)
            makeMove(tmp, c)
            # print("tmp board=", tmp.board)
            ns += [tmp]
            # print("ns=", ns)
    # print("returns ns ", ns)
    return ns




def makeMove(s, c):
    # Puts mark (for huma. or comp.) in col. c
    # and switches turns.
    # Assumes the move is legal.

    r = 0
    while r < rows and s.board[r][c] == 0:
        r += 1

    # TODO add
    s.col = c
    s.row = r

    s.board[r - 1][c] = s.playTurn  # marks the board
    s.size -= 1  # one less empty cell
    if (s.playTurn == COMPUTER):
        s.playTurn = HUMAN
    else:
        s.playTurn = COMPUTER




def inputMove(s):
    # Reads, enforces legality and executes the user's move.

    # self.printState()
    flag = True
    while flag:
        c = int(input("Enter your next move: "))
        if c < 0 or c >= columns or s.board[0][c] != 0:
            print("Illegal move.")

        else:
            flag = False
            makeMove(s, c)

#def inputMove(s):
#    score, new_s = alphaBetaPruning.go(s, computer_two.value)
#    makeMove(s, new_s.col)
#    return score

def inputComputer(s:game):
    score, new_s = alphaBetaPruning.go(s, computer_one.value)
    makeMove(s,new_s.col)
    return score