import random

def get_computer_move(): # randomly selects the value of the computer
    return "rps"[random.randint(0,2)]

def determine_winner(player_move, comp_move): # compares the player's value to the computer's value
    if player_move == comp_move:
        return "It's a tie"
    elif (player_move == "r" and comp_move == "s") or \
         (player_move == "s" and comp_move == "p") or \
         (player_move == "p" and comp_move == "r"):
        return "Player wins"
    else:
        return "Player loses"

def avgPercentWin(): # selects 3 numbers and averages them to get a percentage
    # data = [random.randint(0, 99) + 1, random.randint(0, 99) + 1, random.randint(0, 99) + 1]
    # x = statistics.mean(data)
    # return x
    
    # do stats to make it more difficult
    return avg

def hal_9000(player_move, comp_move, avgPercentWin):
    if avgPercentWin > 33: # this is a black box, change it
        return "Player loses"
    else:
        return determine_winner(player_move, comp_move)

def player_wins(result): # counts the player's wins
    if result == "Player wins":
        return 1
    else:
        return 0

def player_losses(result):
    if result == "Player loses":
        return 1
    else:
        return 0

def player_ties(result):
    if result == "It's a tie":
        return 1
    else:
        return 0