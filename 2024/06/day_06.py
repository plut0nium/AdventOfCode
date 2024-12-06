#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import defaultdict
from copy import copy, deepcopy

OBSTRUCTION = "#"
GUARD = "^"
DIRECTIONS = [(0,-1), (1,0), (0,1), (-1,0)] # N > E > S > W

def part1(grid, grid_size, start_position):
    x, y = start_position
    dir_idx = 0
    path = set()
    path.add((x,y))
    while True:
        x_new = x + DIRECTIONS[dir_idx][0]
        y_new = y + DIRECTIONS[dir_idx][1]
        if (x_new < 0) or (x_new >= grid_size[0]) \
           or (y_new < 0) or (y_new >= grid_size[1]):
            # out of grid
            break
        elif (x_new, y_new) in grid:
            dir_idx = (dir_idx + 1) % len(DIRECTIONS)
        else:
            x, y = x_new, y_new
            path.add((x,y))
    return len(path)


def part2(grid, grid_size, start_position):
    x, y = start_position
    dir_idx = 0
    new_obst = set()
    path = defaultdict(set)
    while True:
        path[(x,y)].add(dir_idx)
        x_new = x + DIRECTIONS[dir_idx][0]
        y_new = y + DIRECTIONS[dir_idx][1]
        if (x_new < 0) or (x_new >= grid_size[0]) \
           or (y_new < 0) or (y_new >= grid_size[1]):
            # out of grid
            break
        elif (x_new, y_new) in grid:
            dir_idx = (dir_idx + 1) % len(DIRECTIONS)
        else:
            x, y = x_new, y_new

        # check if next position can be a new obstruction
        x_obst = x + DIRECTIONS[dir_idx][0]
        y_obst = y + DIRECTIONS[dir_idx][1]
        if (x_obst,y_obst) in grid \
           or (x_obst,y_obst) == start_position \
           or (x_obst,y_obst) in path:
            # obstruction not allowed here
            continue
        if not(0 <= x_obst < grid_size[0]) \
           or not(0 <= y_obst < grid_size[1]):
            # out of grid
            continue
        # create a copy of current path
        # path2 = deepcopy(path) # EXTREMELY slow !
        path2 = defaultdict(set) # still slow but not as much
        for k,v in path.items():
            path2[k] = set(v)
        x2, y2 = x, y
        dir_idx2 = (dir_idx + 1) % len(DIRECTIONS)
        while True:
            if dir_idx2 in path2[(x2,y2)]:
                # already went through this position in the same direction
                # -> loop found
                new_obst.add((x_obst,y_obst))
                break
            path2[(x2,y2)].add(dir_idx2)
            x_new = x2 + DIRECTIONS[dir_idx2][0]
            y_new = y2 + DIRECTIONS[dir_idx2][1]
            if (x_new < 0) or (x_new >= grid_size[0]) \
               or (y_new < 0) or (y_new >= grid_size[1]):
                # out of grid
                break
            elif (x_new,y_new) in grid \
                 or (x_new,y_new) == (x_obst,y_obst):
                dir_idx2 = (dir_idx2 + 1) % len(DIRECTIONS)
                continue
            else:
                x2, y2 = x_new, y_new
    return len(new_obst)


if __name__ == '__main__':
    grid = {}
    start_position = None
    with open(input_file, 'r') as f:
        for y, l in enumerate(f.readlines()):
            for x, p in enumerate(l.strip()):
                if p == OBSTRUCTION:
                    grid[(x,y)] = OBSTRUCTION
                elif p == GUARD:
                    start_position = (x,y)
                else:
                    pass
        grid_size = (x+1, y+1)
    print(part1(grid, grid_size, start_position))
    print(part2(grid, grid_size, start_position))
