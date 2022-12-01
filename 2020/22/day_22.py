#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from copy import deepcopy

GAME_ID = 0

def crab_combat(decks, recursive=False):
    if recursive:
        # global GAME_ID
        # GAME_ID += 1
        # gid = GAME_ID
        # print("Starting game ", gid)
        past_rounds = [[],[]]
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        c1 = decks[0].popleft()
        c2 = decks[1].popleft()
        if recursive:
            if any(','.join(map(str,decks[i])) in past_rounds[i] for i in range(2)): # anti recursion rule
                return [[1],[]] # will be evaluated as a win for Player 1
            else:
                for i in range(2):
                    past_rounds[i].append(','.join(map(str,decks[i])))
            if len(decks[0]) >= c1 and len(decks[1]) >= c2:
                decks_recursed = crab_combat(deepcopy(decks), True)
                if len(decks_recursed[0]):
                    decks[0].extend((c1, c2))
                else:
                    decks[1].extend((c2, c1))
                continue
        if c1 > c2:
            decks[0].extend((c1, c2))
        else:
            decks[1].extend((c2, c1))
    return decks
    

input_file = "input"
# input_file = "test1.txt"

if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        decks = [deque(c for c in map(int,d.split('\n')[1:])) for d in f.read().strip().split('\n\n')]
    
    decks_backup = deepcopy(decks)
    n_cards = len(decks[0]) + len(decks[1]) 
    
    # part 1
    decks = crab_combat(decks)

    if len(decks[0]):
        winning_deck = decks[0]
    else:
        winning_deck = decks[1]

    for i, c in enumerate(winning_deck):
        count1 += c * (n_cards - i)
    
    # part 2
    decks = decks_backup

    decks = crab_combat(decks, recursive=True)

    if len(decks[0]):
        winning_deck = decks[0]
    else:
        winning_deck = decks[1]

    for i, c in enumerate(winning_deck):
        count2 += c * (n_cards - i)

    print("Step 1:", count1)
    print("Step 2:", count2)

