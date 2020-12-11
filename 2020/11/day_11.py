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
    count = 0
    grid_x = len(grid[0])
    grid_y = len(grid)
    working_grid = deepcopy(grid)
    while True:
        new_grid = deepcopy(working_grid)
        seats_changed = 0
        for x,y in product(range(grid_x),range(grid_y)):
            if grid[y][x] == '.':
                continue
            os =  count_occupied_seats(x, y, working_grid, radius)
            if working_grid[y][x] == 'L' and os == 0:
                new_grid[y][x] = '#'
                seats_changed += 1
            elif working_grid[y][x] == '#' and os >= tolerance:
                new_grid[y][x] = 'L'
                seats_changed += 1
        # print_grid(new_grid)
        # print(seats_changed)
        working_grid = new_grid
        if seats_changed == 0:
            for r in working_grid:
                count += r.count('#')
            break
    return count

def print_grid(g):
    for r in g:
        print(' '.join(str(c) for c in r))


if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        grid = [[c for c in l.strip()] for l in f.readlines() if l.strip()]

    count1 = populate_seats(grid)
    count2 = populate_seats(grid, None, 5)

    print("Step 1:", count1)
    print("Step 2:", count2)

