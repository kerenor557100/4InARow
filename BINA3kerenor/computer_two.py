# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:34:11 2020

@author: keren or
"""
#In this exercise, 
#we were asked to exercise the game so that victory / loss / tie situations would be identified.
# What I've done here is that there is a possibility that a human can play against a 
#computer or two computers play against each other.
import copy
import random

VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1
# turn_factor = {HUMAN: -10, COMPUTER: 8}
turn = {HUMAN: COMPUTER, COMPUTER: HUMAN}

rows = 6
columns = 7

param = \
    {"horizontal": {'func': lambda i,board: board[i], 'index_to': rows},
    "vertical": {'func': lambda i,board: map(lambda x: x[i], board), 'index_to': columns},
    "pos": {'func': lambda i,board: diagonal_gen(board, i), "index_from": -rows + 1, 'index_to': columns},
    "neg": {'func': lambda i,board: diagonal_gen(board, i, False), "index_from": -rows + 1,'index_to': columns}}


# @print_decoration
def value(s):
    # Returns the heuristic value of s
    # if find_horizontal(s) or find_vertical(s) or find_neg_diagonal(s) or find_pos_diagonal(s):
    if any(map(lambda args: find_rows(s, **args), param.values())):
        #TODO add
        s.movs[s.col] = s.playTurn
        return VICTORY if s.playTurn == HUMAN else LOSS
    if s.size == 0:
        return TIE
    return random.random() * 10

def max_len(_list, num):
    count = 0
    max_count = 0
    for item in _list:
        count = count + 1 if item == num else 0
        max_count = max(count, max_count)
        if max_count >= SIZE:
            break
    return max_count


def find_rows(s, func, index_from=0, index_to=0):
    return any(map(lambda i: max_len(func(i,s.board), turn[s.playTurn]) >= SIZE, range(index_from, index_to)))

def diagonal_gen(board, start_index, is_pos=True):
    row_func = (lambda i: i) if is_pos else (lambda i: rows - 1 - i)
    current_column = start_index if start_index >= 0 else 0
    current_row = 0 if start_index >= 0 else -start_index
    while current_column < columns and current_row < rows:
        yield board[row_func(current_row)][current_column]
        current_column += 1
        current_row += 1