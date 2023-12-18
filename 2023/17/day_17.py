#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

START = (0,0)
DIRS = [(1,0), (0,-1), (-1,0), (0,1)] # left, up, right, down

import numpy as np
from heapq import heappush, heappop

def parse_city(input_lines):
    city = []
    for l in input_lines:
        city.append([int(i) for i in l.strip()])
    return np.array(city)

def in_grid(grid, pos):
    x_max, y_max = grid.shape
    return 0 <= pos[0] < x_max and 0 <= pos[1] < y_max 

def find_path(city, start, end, move_min=0, move_max=3):
    heap = [(0, start, (0,0))] # heat_loss, position, direction_counter
    visited = set()
    
    while len(heap):
        heat_loss, pos, dir_counter = heappop(heap)
        for dir_idx in range(len(DIRS)):
            if dir_idx == 2: # backwards <- EXCLUDED
                continue
            elif dir_idx == 0: # we do not change direction
                if dir_counter[1] == move_max:
                    # already move_max in this direction, we have to turn
                    continue
                else:
                    # increment counter
                    dc = dir_counter[1] + 1
            else: # 1 or 3 = turn
                if dir_counter[1] < move_min:
                    # part 2: we cannot change direction if we did not move
                    # at least move_min
                    continue
                # reset counter
                dc = 1
            dir_idx_new = (dir_counter[0] + dir_idx) % len(DIRS)
            dir_counter_update = (dir_idx_new, dc)
            pos_new = (pos[0] + DIRS[dir_idx_new][0], pos[1] + DIRS[dir_idx_new][1])
            if in_grid(city, pos_new) and (pos_new, dir_counter_update) not in visited:
                heat_loss_new = heat_loss + city[pos_new]
                if pos_new == end:
                    # we reached the end
                    return heat_loss_new
                visited.add((pos_new, dir_counter_update))
                heappush(heap,(heat_loss_new, pos_new, dir_counter_update))

@timing
def part1(city):
    end = tuple(map(lambda x: x-1, city.shape))
    return find_path(city, START, end)

@timing
def part2(city):
    end = tuple(map(lambda x: x-1, city.shape))
    return find_path(city, START, end, 4, 10)


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        city = parse_city(f.readlines())
    print("Part #1 :", part1(city))
    print("Part #2 :", part2(city))
