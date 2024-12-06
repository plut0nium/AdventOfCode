#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import defaultdict

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

    return None


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
