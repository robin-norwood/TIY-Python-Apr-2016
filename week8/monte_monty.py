# Create simulation of the monty hall problem. Run the simulation many times to determine if there is a winning strategy.
#
# Three doors
# Player (p) picks a door.
# Host (h) reveals a goat behind one of the other two doors.
# Player either:
#  1) Stays
#  2) Switches
# Player either wins or loses.

import random

DOOR_1 = 1
DOOR_2 = 2
DOOR_3 = 3

doors = (DOOR_1, DOOR_2, DOOR_3)

STRATEGY_SWITCH = 'switch'
STRATEGY_STAY = 'stay'

def strategy_stay(init_choice, goat_door):
    return init_choice

def strategy_switch(init_choice, goat_door):
    my_doors = list(doors[:])
    my_doors.remove(init_choice)
    my_doors.remove(goat_door)

    return my_doors[0]

def pick_a_door():
    return random.choice(doors)

def pick_goat_door(init_choice, prize_door):
    my_doors = list(doors[:])
    my_doors.remove(init_choice)
    if prize_door in my_doors:
        my_doors.remove(prize_door)

    return random.choice(my_doors)

## Play the game
def play_round(strategy):
    prize_door = pick_a_door()
    player_choice = pick_a_door()

    goat_door = pick_goat_door(player_choice, prize_door)
    new_choice = None
    if strategy == STRATEGY_SWITCH:
        new_choice = strategy_switch(player_choice, goat_door)
    if strategy == STRATEGY_STAY:
        new_choice = strategy_stay(player_choice, goat_door)

    did_player_win = new_choice == prize_door

    return did_player_win

stay_wins = 0
switch_wins = 0

PLAYS = 100000

for x in range(PLAYS):
    won = play_round(STRATEGY_STAY)
    if won:
        stay_wins += 1

    won = play_round(STRATEGY_SWITCH)
    if won:
        switch_wins += 1

print("STRAT: Stay - " + str(stay_wins) + " wins - " + str(round(stay_wins/PLAYS, 2) * 100) + " pct")
print("STRAT: Switch - " + str(switch_wins) + " wins - " + str(round(switch_wins/PLAYS, 2) * 100) + " pct")
