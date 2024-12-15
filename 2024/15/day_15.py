#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
input_file = "test01.txt"
# input_file = "test02.txt"
input_file = "test03.txt"


from collections import defaultdict
from itertools import chain
from copy import copy

DIRS = { "^": ( 0,-1),
         ">": ( 1, 0),
         "v": ( 0, 1),
         "<": (-1, 0) }

WALL = "#"
CRATE = "O"
ROBOT = "@"
EMPTY = "."
BIG_CRATE = "[]"


def gps(x, y):
    return x + y * 100


def print_warehouse(warehouse):
    for y in range(max(c[1] for c in warehouse.keys()) + 1):
        for x in range(max(c[0] for c in warehouse.keys()) + 1):
            print(warehouse[(x,y)], end="")
        print()        


def enlarge_warehouse(warehouse):
    warehouse_big = defaultdict(lambda : EMPTY)
    for y in range(max(c[1] for c in warehouse.keys()) + 1):
        for x in range(max(c[0] for c in warehouse.keys()) + 1):
            if warehouse[(x,y)] == WALL:
                new = WALL * 2
            elif warehouse[(x,y)] == CRATE:
                new = BIG_CRATE
            elif warehouse[(x,y)] == ROBOT:
                new = ROBOT + EMPTY
            else:
                continue
            for i in range(len(new)):
                warehouse_big[(x*2 + i, y)] = new[i]
    return warehouse_big


def part1(warehouse, moves, initial_position):
    robot_pos = initial_position
    warehouse = copy(warehouse)
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
    # print_warehouse(warehouse)
    return sum(gps(*coord) for coord, item in warehouse.items() if item == CRATE)


def part2(warehouse, moves, initial_position):
    warehouse = enlarge_warehouse(warehouse)
    robot_pos = initial_position[0] * 2, initial_position[1]
    for m in moves:
        print(m)
        x, y = robot_pos
        lov = [(ROBOT, (x,y))]
        if m in ("<", ">"):
            # horizontal move -> proceed as part 1
            while True:
                x_next = x + DIRS[m][0]
                y_next = y + DIRS[m][1]
                lov.append((warehouse[(x_next, y_next)], (x_next, y_next)))
                if warehouse[(x_next, y_next)] == WALL:
                    break
                x, y = x_next, y_next
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
        else:
            # vertical move
            fov = [lov]
            blocked = False
            while True:
                fov.append([])
                for item in fov[-2]:
                    x,y = item[1]
                    x_next = x + DIRS[m][0]
                    y_next = y + DIRS[m][1]
                    if warehouse[(x_next, y_next)] == BIG_CRATE[0]:
                        fov[-1].append((BIG_CRATE[0], (x_next, y_next)))
                        fov[-1].append((BIG_CRATE[1], (x_next+1, y_next)))
                    elif warehouse[(x_next, y_next)] == BIG_CRATE[1]:
                        fov[-1].append((BIG_CRATE[0], (x_next-1, y_next)))
                        fov[-1].append((BIG_CRATE[1], (x_next, y_next)))
                    else:
                        fov[-1].append((warehouse[(x_next, y_next)], (x_next, y_next)))
                if any(item[0] == WALL for item in fov[-1]):
                    blocked = True
                    break
                if all(item[0] == EMPTY for item in fov[-1]):
                    break
            if blocked:
                print("Blocked!")
                continue
            items_to_move = list(chain(*fov))
            # print(items_to_move)
            for item in items_to_move:
                if item[0] == EMPTY:
                    continue
                warehouse[item[1]] = EMPTY
            for item in items_to_move:
                if item[0] == EMPTY:
                    continue
                dest = (item[1][0], item[1][1] + DIRS[m][1])
                warehouse[dest] = item[0]
                if item[0] == ROBOT:
                    robot_pos = dest
            print_warehouse(warehouse)
    print_warehouse(warehouse)
    return sum(gps(*coord) for coord, item in warehouse.items() if item == BIG_CRATE[0])


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
    print(part2(warehouse, moves, initial_position))
