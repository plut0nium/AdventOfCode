#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
from itertools import product
from copy import deepcopy

input_file = "input"
# input_file = "test1.txt"

def count_occupied_seats(x, y, grid, radius=None):
    directions = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    count = 0
    grid_x = len(grid[0])
    grid_y = len(grid)
    for d in directions:
        r = 1
        a,b = x,y
        while True:
            a += d[0]
            b += d[1]
            if a not in range(grid_x) or b not in range(grid_y):
                break
            if grid[b][a] == '#':
                count += 1
            if grid[b][a] != '.':
                break
            if radius is not None:
                if r >= radius:
                    break
                else:
                    r += 1
    return count

def populate_seats(grid, radius=1, tolerance=4):
    grid_x = len(grid[0])
    grid_y = len(grid)
    grid_populated = deepcopy(grid)
    while True:
        grid_update = deepcopy(grid_populated)
        seats_changed = 0
        for x,y in product(range(grid_x),range(grid_y)):
            if grid[y][x] == '.':
                continue
            os =  count_occupied_seats(x, y, grid_populated, radius)
            if grid_populated[y][x] == 'L' and os == 0:
                grid_update[y][x] = '#'
                seats_changed += 1
            elif grid_populated[y][x] == '#' and os >= tolerance:
                grid_update[y][x] = 'L'
                seats_changed += 1
        # print_grid(grid_update)
        # print(seats_changed)
        grid_populated = grid_update
        if seats_changed == 0:
            return grid_populated
    return False

def print_grid(g):
    for r in g:
        print(' '.join(str(c) for c in r))


if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        grid = [[c for c in l.strip()] for l in f.readlines() if l.strip()]

    count1 = sum(r.count('#') for r in populate_seats(grid))
    count2 = sum(r.count('#') for r in populate_seats(grid, None, 5))

    print("Step 1:", count1)
    print("Step 2:", count2)

