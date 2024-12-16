#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"


from collections import defaultdict
from itertools import chain
from copy import copy
import sys

DIRS = [ ( 0,-1), ( 1, 0), ( 0, 1), (-1, 0) ] # N > E > S > W

WALL = "#"
EMPTY = "."
START = "S"
END = "E"


def get_next_steps(pos, dir):
    next_steps = []
    x,y = pos
    for i in (0, 1, -1):
        dir_index = (dir + i) % len(DIRS)
        next_dir = DIRS[dir_index]
        x_next = x + next_dir[0]
        y_next = y + next_dir[1]
        next_steps.append(((x_next, y_next), dir_index))
    return next_steps


def path_score(path):
    score = 0
    for i, p in enumerate(path):
        if i == 0:
            continue
        else:
            if path[i][1] != path[i-1][1]:
                score += 1001
            else:
                score += 1
    return score


def part1(maze, start, end):
    pos = start
    dir = 1 # East
    candidates = [[(pos, dir)]]
    found_paths = []
    while len(candidates):
        # print(candidates)
        current_path = candidates.pop()
        for next_step in get_next_steps(*current_path[-1]):
            if maze[next_step[0]] == WALL:
                continue
            if next_step[0] in [p[0] for p in current_path]:
                # already in path
                continue
            this_path = current_path[:]
            this_path.append(next_step)
            if next_step[0] == end:
                found_paths.append(this_path)
                print(len(found_paths))
            else:
                candidates.append(this_path)
    # return len(found_paths)
    return min(path_score(p) for p in found_paths)


def part2(maze, start, end):

    return None


if __name__ == '__main__':
    maze = defaultdict(lambda : EMPTY)
    start = None
    end = None
    with open(input_file, 'r') as f:
        for y, l in enumerate(f.readlines()):
            for x, p in enumerate(l.strip()):
                if p == WALL:
                    maze[(x,y)] = p
                elif p == START:
                    start = (x,y)
                elif p == END:
                    end = (x,y)
    print(part1(maze, start, end))
    print(part2(maze, start, end))