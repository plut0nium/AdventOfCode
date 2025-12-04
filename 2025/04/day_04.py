#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test_01.txt"

DIRS = [(-1,-1), (-1, 0), (-1, 1),
        ( 0,-1),          ( 0, 1),
        ( 1,-1), ( 1, 0), ( 1, 1)]

PAPER_ROLL = "@"

def part1(storage):
    accessible = set()
    for s in storage.keys():
        adjacent = set()
        for d in DIRS:
            if (s[0]+d[0], s[1]+d[1]) in storage:
                adjacent.add((s[0]+d[0], s[1]+d[1]))
        if len(adjacent) < 4:
            accessible.add(s)
    return len(accessible)


def part2(storage):
    occupied = set(storage.keys())
    while True:
        accessible = set()
        for s in occupied:
            adjacent = set()
            for d in DIRS:
                if (s[0]+d[0], s[1]+d[1]) in occupied:
                    adjacent.add((s[0]+d[0], s[1]+d[1]))
            if len(adjacent) < 4:
                accessible.add(s)
        if len(accessible) == 0: # nothing to remove...
            break
        occupied = occupied.difference(accessible)
    return len(storage) - len(occupied)


if __name__ == '__main__':
    storage = {}
    with open(input_file, 'r') as f:
        for r, l in enumerate(f.readlines()):
            for c, s in enumerate(l.strip()):
                if s == PAPER_ROLL:
                    storage[r, c] = s
    print(part1(storage))
    print(part2(storage))