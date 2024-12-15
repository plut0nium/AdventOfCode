#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"


from collections import defaultdict
from itertools import chain

DIRS = { "^": ( 0,-1),
         ">": ( 1, 0),
         "v": ( 0, 1),
         "<": (-1, 0) }

WALL = "#"
CRATE = "O"
ROBOT = "@"
EMPTY = "."


def gps(x, y):
    return x + y * 100


def print_warehouse(warehouse):
    for y in range(max(c[1] for c in warehouse.keys()) + 1):
        for x in range(max(c[0] for c in warehouse.keys()) + 1):
            print(warehouse[(x,y)], end="")
        print()        


def part1(warehouse, moves, initial_position):
    robot_pos = initial_position
    for m in moves:
        x, y = robot_pos
        lov = [(ROBOT, (x,y))]
        while True:
            x_next = x + DIRS[m][0]
            y_next = y + DIRS[m][1]
            lov.append((warehouse[(x_next, y_next)], (x_next, y_next)))
            if warehouse[(x_next, y_next)] == WALL:
                break
            x, y = x_next, y_next
        # print(lov)
        for i, p in enumerate(lov):
            if p[0] == WALL:
                break
            elif p[0] == EMPTY:
                # move everything in line
                for j in range(i, 0, -1):
                    warehouse[lov[j][1]] = lov[j-1][0]
                warehouse[lov[0][1]] = EMPTY
                robot_pos = lov[1][1]
                break
        # print(m)
        # print_warehouse(warehouse)
    print_warehouse(warehouse)
    return sum(gps(*coord) for coord, item in warehouse.items() if item == CRATE)


def part2(machines):

    return None


if __name__ == '__main__':
    warehouse = defaultdict(lambda : EMPTY)
    initial_position = None
    with open(input_file, 'r') as f:
        warehouse_str, moves_str = f.read().split("\n\n")
        for y, l in enumerate(warehouse_str.splitlines()):
            for x, p in enumerate(l.strip()):
                if p != EMPTY:
                    warehouse[(x,y)] = p
                if p == ROBOT:
                    initial_position = (x,y)
        moves = list(chain(*moves_str.splitlines()))
    print(part1(warehouse, moves, initial_position))
    print(part2(warehouse))
