#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from collections import defaultdict

input_file = "input"
input_file = "test01.txt"

n = 2022
n2 = 1_000_000_000_000

rocks = [ ((0,0), (1,0), (2,0), (3,0)),        # -
          ((1,0), (0,1), (1,1), (2,1), (1,2)), # +
          ((0,0), (1,0), (2,0), (2,1), (2,2)), # L (inverted)
          ((0,0), (0,1), (0,2), (0,3)),        # |
          ((0,0), (1,0), (0,1), (1,1)) ]       # square

moves = {'<': (-1,0), '>': (1,0)}

def rock(c, r):
    # return coordinates of the block elements given c (lower left)
    return tuple(tuple(map(sum, zip(c, b))) for b in r)

def push(c, r, j, cave):
    # attempt to move rock according to jet
    c2 = tuple(map(sum, zip(c, moves[j])))
    if any((xy[0] < 0 or xy[0] > 6 or cave[xy] == '#') for xy in rock(c2, r)):
        # cannot move
        return c
    # return the new coordinates of the rock block
    return c2

def pile_height(cave):
    if len(cave) == 0:
        return -1
    return max(c[1] for c, v in cave.items() if v == '#')

def render(cave):
    for y in range(pile_height(cave), -1, -1):
        r = '|' + ''.join(cave[(x,y)] for x in range(7)) + '|' + str(y)
        print(r)
    print('+-------+')

def pyroclastic_flow(n, jets, cave=None):
    if cave is None:
        cave = defaultdict(lambda: ' ')
    j = 0
    for i in range(n):
        r = rocks[i % len(rocks)]
        h = pile_height(cave) + 4
        c = (2, h) # starting coordinates of the block
        while True:
            # move sideways
            c2 = push(c, r, jets[j], cave)
            j = (j + 1) % len(jets)
            # move downwards
            c3 = tuple(map(sum, zip(c2, (0,-1))))
            if any(cave[y] == '#' or y[1] < 0 for y in rock(c3, r)):
                # rock cannot fall anymore -> next
                for z in rock(c2, r):
                    cave[z] = '#'
                break
            else:
                c = c3
    return cave

if __name__ == '__main__':
    start_time = time()
    jets = [c for c in open(input_file, 'r').read().strip() if c in ('<','>')]


    print("Part #1 :", pile_height(pyroclastic_flow(n, jets))+1)
    
    # TODO

        
    print("Part #2 :", None)
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
