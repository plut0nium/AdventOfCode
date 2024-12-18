#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from utils import timing

from heapq import heappush, heappop

DIRS = [ ( 0,-1), ( 1, 0), ( 0, 1), (-1, 0) ] # N > E > S > W

BLOCK = "#"
EMPTY = "."
PATH = "o"
START = (0, 0)
if "test" in input_file:
    BYTE_COUNT = 12
    END = (6, 6)
else:
    BYTE_COUNT = 1024
    END = (70, 70)


def print_grid(grid, size, path=None):
    for y in range(size[1] + 1):
        for x in range(size[0] + 1):
            if (x,y) in grid:
                print(BLOCK, end="")
            elif path is not None \
               and (x,y) in path:
                print(PATH, end="")
            else:
                print(EMPTY, end="")
        print()
    return None


def dist(a, b):
    # return abs(a[0] - b[0]) + abs(a[1] - b[1]) 
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def find_path(grid, start, end):
    queue = []
    heappush(queue, (dist(start, end), [start, ]))
    visited = {}
    while len(queue):
        _, path = heappop(queue)
        x, y = path[-1]
        for d in DIRS:
            x_next = x + d[0]
            y_next = y + d[1]
            if not (0 <= x_next <= end[0]) \
               or not (0 <= y_next <= end[1]):
                continue
            if (x_next, y_next) in path \
               or (x_next, y_next) in grid:
                continue
            if (x_next, y_next) in visited \
               and visited[(x_next, y_next)] <= len(path) + 1:
                continue
            visited[(x_next, y_next)] = len(path) + 1
            if (x_next, y_next) == end:
                print_grid(grid, END, path + [(x_next, y_next)])
                return path + [(x_next, y_next)]
            else:
                heappush(queue, (dist((x_next, y_next), END),
                                 path + [(x_next, y_next)]))
    return None


@timing
def part1(byte_list):
    grid = {b:BLOCK for b in byte_list[:BYTE_COUNT]}
    return len(find_path(grid, START, END)) - 1


@timing
def part2(byte_list):
    # grid = {b:BLOCK for b in byte_list[:BYTE_COUNT]}
    # path = find_path(grid, START, END)
    # for b in byte_list[BYTE_COUNT:]:
    #     grid[b] = BLOCK
    #     if b not in path:
    #         continue
    #     path = find_path(grid, START, END)
    #     if path is None:
    #         return ",".join(map(str, b))
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        byte_list = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]
    print(part1(byte_list))
    print(part2(byte_list))
