# TIC-TAC-TOE logic in numpy python, selfmade, learned new method of numpy i.e. np.all() for boolean values

import numpy as np

playground = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
game = np.array(playground, dtype=object)

x = 'player-X'
o = 'player-O'
print(game)

def win_condition(game, symbol):
    # Rows
    if np.all(game[0, :] == symbol):
        return True
    if np.all(game[1, :] == symbol):
        return True
    if np.all(game[2, :] == symbol):
        return True
    # columns
    if np.all(game[:, 0] == symbol):
        return True
    if np.all(game[:, 1] == symbol):
        return True
    if np.all(game[:, 2] == symbol):
        return True
    # diagonals
    if np.all(np.array([game[0,0],game[1,1],game[2,2]]) == symbol):
        return True
    if np.all(np.array([game[2,0],game[1,1],game[0,2]]) == symbol):
        return True
    
def draw_condition(game):
    if np.all(game != ' '):
        return True

def turn_mechanism(game, player, symbol):
    user_input = input(f'\n{player.title()} please enter corrdinates: ')
    if game[int(user_input[0]), int(user_input[1])] == ' ':
        game[int(user_input[0]), int(user_input[1])] = symbol
        print(game)
    else:
        print('invaild, field was filled')
        turn_mechanism(game, player, symbol)
    if win_condition(game, symbol) == True:
        print(f'{player.title()} WON')
        exit()
    if draw_condition(game) == True:
        print(f'DRAW')
        exit()
        
while True:
    turn_mechanism(game, x, symbol='X')
    turn_mechanism(game, o, symbol='O')
            