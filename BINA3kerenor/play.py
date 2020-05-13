# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:23:02 2020

@author: keren or
"""
#In this exercise, 
#we were asked to exercise the game so that victory / loss / tie situations would be identified.
# What I've done here is that there is a possibility that a human can play against a 
#computer or two computers play against each other.
import copy
import game
from tqdm import trange

def play_game(first_player,verbos = False):
    board=game.game()
    game.create(board)

    if verbos :
        print("Initial Game")
        game.printState(board)
    game.decideWhoIsFirst(board,first_player)

    while not game.isFinished(board):
        score = 0
        if game.isHumTurn(board):
            score = game.inputMove(board)
        else:
            score = game.inputComputer(board)
        if verbos :
            print("continue game")
            game.printState(board)
            print(f"score: {score}")
    return game.who_won(board)

COMPUTER = 5
HUMAN = 1

game_result = dict()
def run_game(first_player,num):
    for i in trange(num):
        result = play_game(first_player)
        if result in game_result.keys():
            game_result[result] +=1
        else:
            game_result[result] = 1



#run_game(HUMAN,1000)

#print(f"result: {game_result}")

print(play_game(COMPUTER,True))
