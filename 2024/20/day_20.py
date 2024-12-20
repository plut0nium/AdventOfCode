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

from collections import deque, Counter

DIRS = [ ( 0,-1), ( 1, 0), ( 0, 1), (-1, 0) ] # N > E > S > W

START = "S"
END = "E"
WALL = "#"

if "test" in input_file:
    MIN_SHORTCUT = 2
else:
    MIN_SHORTCUT = 100


def find_path(grid, start, end, size):
    queue = deque([[start], ])
    visited = {}
    while len(queue):
        path = queue.popleft()
        x, y = path[-1]
        for d in DIRS:
            x_next = x + d[0]
            y_next = y + d[1]
            if not (0 <= x_next <= size[0]) \
               or not (0 <= y_next <= size[1]):
                continue
            if (x_next, y_next) in path \
               or (x_next, y_next) in grid:
                continue
            if (x_next, y_next) in visited \
               and visited[(x_next, y_next)] <= len(path) + 1:
                continue
            visited[(x_next, y_next)] = len(path) + 1
            if (x_next, y_next) == end:
                return path + [(x_next, y_next)]
            else:
                queue.append(path + [(x_next, y_next)])
    return None


def dist_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbours(pos):
    x, y = pos
    return ((x + d[0], y + d[1]) for d in DIRS)


@timing
def part1(racetrack, start, end, size):
    path = find_path(racetrack, start, end, size)
    cheats = set()
    for i, p in enumerate(path):
        for j, q in enumerate(path[i+2:]):
            if dist_manhattan(p, q) > 2:
                continue
            if path.index(q) - path.index(p) - dist_manhattan(p, q) >= MIN_SHORTCUT:
                cheats.add((p,q))
    return Counter(path.index(q) - path.index(p) - dist_manhattan(p, q) for p, q in cheats).total()


@timing
def part2(racetrack, start, end, size):

    return None


if __name__ == '__main__':
    racetrack = {}
    start = None
    end = None
    size = None
    with open(input_file, 'r') as f:
        for y, r in enumerate(f.readlines()):
            for x, v in enumerate(r.strip()):
                if v == WALL:
                    racetrack[(x,y)] = WALL
                elif v == START:
                    start = (x,y)
                elif v == END:
                    end = (x,y)
        size = (x,y)
    print(part1(racetrack, start, end, size))
    print(part2(racetrack, start, end, size))
