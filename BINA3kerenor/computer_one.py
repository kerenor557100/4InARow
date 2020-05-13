# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:33:41 2020

@author: keren or
"""
#In this exercise, 
#we were asked to exercise the game so that victory / loss / tie situations would be identified.
# What I've done here is that there is a possibility that a human can play against a 
#computer or two computers play against each other.
import copy

# from game import game

VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1

location_factor = 4



com_s = {0:1,1:20,2:200,3:400}
turn_factor = -0.9
hum_s = {k:v*turn_factor for k,v in com_s.items()}

rows = 6
columns = 7


def print_decoration(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        print(f"result: {result}")
        return result
    return wrapper


param = \
    {"horizontal": {'func': lambda i,board: board[i], 'index_to': rows},
    "vertical": {'func': lambda i,board: map(lambda x: x[i], board), 'index_to': columns},
    "pos": {'func': lambda i,board: diagonal_gen(board, i), "index_from": -rows + 1, 'index_to': columns},
    "neg": {'func': lambda i,board: diagonal_gen(board, i, False), "index_from": -rows + 1,'index_to': columns}}


# @print_decoration
def value(s):
    # Returns the heuristic value of s
    # if find_horizontal(s) or find_vertical(s) or find_neg_diagonal(s) or find_pos_diagonal(s):
    score = sum(map(lambda args: sum_rows(s, **args), param.values()))
    # print(f"playTurn: {turn[s.playTurn]},score: {score}")
    if score >= VICTORY:
        s.movs[s.col] = COMPUTER
        return VICTORY
    if score <= LOSS:
        s.movs[s.col] = HUMAN
        return LOSS
    if s.size == 0:
        return TIE
    return score#*turn_factor[turn[s.playTurn]]


def sum_rows(s, func, index_from=0, index_to=0):
    return sum(map(lambda i: line_score(func(i,s.board)), range(index_from, index_to)))


def diagonal_gen(board, start_index, is_pos=True):
    row_func = (lambda i: i) if is_pos else (lambda i: rows - 1 - i)
    current_column = start_index if start_index >= 0 else 0
    current_row = 0 if start_index >= 0 else -start_index
    while current_column < columns and current_row < rows:
        yield board[row_func(current_row)][current_column]
        current_column += 1
        current_row += 1


def line_score(it):
    sum = 0.00001
    _list = list(it)
    _list_size = len(_list)
    for i in range(_list_size-SIZE+1):
        location_score = int(_list_size/2 - abs(_list_size/2-i))*location_factor
        current_list = _list[i:i+SIZE]
        count_empty = current_list.count(0)
        count_computer = current_list.count(COMPUTER)
        count_human = current_list.count(HUMAN)
        if count_computer == SIZE:
            return VICTORY
        if count_human == SIZE:
            return LOSS
        if  count_empty+count_computer == SIZE:# and count_num>0:
            sum += com_s[count_computer] + location_score

        if count_empty + count_human == SIZE:  # and count_num>0:
            sum += hum_s[count_human] + location_score
        # first_empty = current_list.index(0)+i
        # _list[first_empty] = -1
    return sum



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

# @print_decoration
# def value(s:game):
#     # Returns the heuristic value of s
#     # if find_horizontal(s) or find_vertical(s) or find_neg_diagonal(s) or find_pos_diagonal(s):
#     if any(map(lambda args: find_rows(s, **args), param.values())):
#         #TODO add
#         s.movs[s.col] = s.playTurn
#         return VICTORY if s.playTurn == HUMAN else LOSS
#     if s.size == 0:
#         return TIE
#     return random.random() * 10


# def find_horizontal(s: game):
#     turn = {HUMAN: COMPUTER, COMPUTER: HUMAN}
#     return any(map(lambda i: max_len(s.board[i], turn[s.playTurn]) >= SIZE, range(rows)))
#
#
# def find_vertical(s):
#     turn = {HUMAN: COMPUTER, COMPUTER: HUMAN}
#     vertical_func = lambda i: map(lambda x: x[i], s.board)
#     return any(map(lambda i: max_len(vertical_func(i), turn[s.playTurn]) >= SIZE, range(columns)))
#
# def find_pos_diagonal(s):
#     turn = {HUMAN: COMPUTER, COMPUTER: HUMAN}
#     return any(map(lambda i: max_len(diagonal_gen(s.board,i), turn[s.playTurn]) >= SIZE, range(-rows+1,columns)))
#
# def find_neg_diagonal(s):
#     turn = {HUMAN: COMPUTER, COMPUTER: HUMAN}
#     return any(map(lambda i: max_len(diagonal_gen(s.board,i,False), turn[s.playTurn]) >= SIZE, range(-rows+1,columns)))



# def neg_diagonal_gen(board,start_index):
#     current_column = start_index if start_index >= 0 else 0
#     current_row = rows-1 if start_index >= 0 else rows + start_index - 1
#     while current_column < columns and current_row >= 0:
#         yield board[current_row][current_column]
#         current_column += 1
#         current_row -= 1


# def line_score1(it, num):
#     sum = 0.00001
#     _list = list(it)
#     _list_size = len(_list)
#     for i in range(_list_size-SIZE+1):
#         location_score = int(_list_size/2 - abs(_list_size/2-i))*location_factor
#         current_list = _list[i:i+SIZE]
#         count_empty = current_list.count(0)
#         count_num = current_list.count(num)
#         if count_num == SIZE:
#             return VICTORY
#         if  count_empty+count_num == SIZE:# and count_num>0:
#             sum += sequence_factor[count_num] + location_score
#             # first_empty = current_list.index(0)+i
#             # _list[first_empty] = -1
#     return sum



# _list= [[1,2,3,4,5,6,7],
#         [10,20,30,40,50,60,70],
#         [100,200,300,400,500,600,700],
#         [1000,2000,3000,4000,5000,6000,7000],
#         [10000,20000,30000,40000,50000,60000,70000],
#         [15,25,35,45,55,65,75]]
# for i in range(-2,7):
#     print(list((_list,i,False)))

