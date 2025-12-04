#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from utils import timing

from itertools import chain

NUMERIC_PAD = { "7":( 0, 0), "8":( 1, 0), "9":( 2, 0),
                "4":( 0, 1), "5":( 1, 1), "6":( 2, 1),
                "1":( 0, 2), "2":( 1, 2), "3":( 2, 2),
                "X":( 0, 3), "0":( 1, 3), "A":( 2, 3) }

DIRECTIONAL_PAD = { "X":( 0, 0), "^":( 1, 0), "A":( 2, 0),
                    "<":( 0, 1), "v":( 1, 1), ">":( 2, 1) }

GAP = "X"

MOVES = { ( 0, 1):"^", ( 1, 0):">", ( 0,-1):"v", (-1, 0):"<" }


def dist_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dist(a, b):
    return dist_manhattan(a, b)


def get_robot_input(sequence, robot_type=NUMERIC_PAD, is_robot=True):
    robot_pos = robot_type["A"]
    robot_input = []
    for c in sequence:
        dest = robot_type[c]
        move = (dest[0] - robot_pos[0], dest[1] - robot_pos[1])
        # horizontal moves
        hpush = []
        if move[0] < 0:
            # move left
            h = "<"
        elif move[0] > 0:
            # move right
            h = ">"
        else:
            # no horizontal move
            h = None
        hpush = [h for _ in range(abs(move[0]))]
        # vertical move
        if move[1] > 0:
            # move down
            v = "v"
        elif move[1] < 0:
            # move up
            v = "^"
        else:
            # no vertical move
            v = None
        vpush = [v for _ in range(abs(move[1]))]
        # avoid gap
        if robot_type == NUMERIC_PAD:
            if move[0] < 0 and move[1] < 0 and robot_pos[1] == 3:
                # if we have to go left & up, first go up
                robot_input.extend(chain(vpush, hpush))
            elif move[0] > 0 and move[1] > 0 and robot_pos[0] == 0:
                # if we have to go right & down, first go right
                robot_input.extend(chain(hpush, vpush))
            # elif v is None or h is None:
            else:
                robot_input.extend(chain(vpush, hpush))
            # else:
            #     if sum(dist(a,b) for a,b in ((DIRECTIONAL_PAD["A"], DIRECTIONAL_PAD[h]),
            #                                  (DIRECTIONAL_PAD[h], DIRECTIONAL_PAD[v]),
            #                                  (DIRECTIONAL_PAD[v], DIRECTIONAL_PAD["A"]))) < \
            #        sum(dist(a,b) for a,b in ((DIRECTIONAL_PAD["A"], DIRECTIONAL_PAD[v]),
            #                                  (DIRECTIONAL_PAD[v], DIRECTIONAL_PAD[h]),
            #                                  (DIRECTIONAL_PAD[h], DIRECTIONAL_PAD["A"]))):
            #         robot_input.extend(chain(hpush, vpush))
            #     else:
            #         robot_input.extend(chain(vpush, hpush))
        elif robot_type == DIRECTIONAL_PAD:
            if move[0] < 0 and move[1] > 0 and robot_pos[1] == 1:
                # if we have to go left & down, first go down
                robot_input.extend(chain(vpush, hpush))
            # elif move[0] > 0 and move[1] < 0 and robot_pos[0] == 0:
            #     # if we have to go right & up, first go right
            #     robot_input.extend(chain(hpush, vpush))
            # elif v is None or h is None:
            #     robot_input.extend(chain(hpush, vpush))
            else:
                robot_input.extend(chain(hpush, vpush))
                # if sum(dist(a,b) for a,b in ((DIRECTIONAL_PAD["A"], DIRECTIONAL_PAD[h]),
                #                              (DIRECTIONAL_PAD[h], DIRECTIONAL_PAD[v]),
                #                              (DIRECTIONAL_PAD[v], DIRECTIONAL_PAD["A"]))) <= \
                #    sum(dist(a,b) for a,b in ((DIRECTIONAL_PAD["A"], DIRECTIONAL_PAD[v]),
                #                              (DIRECTIONAL_PAD[v], DIRECTIONAL_PAD[h]),
                #                              (DIRECTIONAL_PAD[h], DIRECTIONAL_PAD["A"]))):
                #     robot_input.extend(chain(hpush, vpush))
                # else:
                #     robot_input.extend(chain(vpush, hpush))
        else:
            raise ValueError(f"Unknown robot type: {robot_type}")
        # activate
        robot_input.append("A")
        robot_pos = dest
    return robot_input


@timing
def part1(codes):
    complexity = []
    for code in codes:
        sequence = [[c for c in code], ]
        for robot_type in [ NUMERIC_PAD,
                            DIRECTIONAL_PAD,
                            DIRECTIONAL_PAD ]:
            sequence.append(get_robot_input(sequence[-1], robot_type))
        for s in sequence:
            print(''.join(c for c in s), len(s))
        complexity.append(len(sequence[-1]) * int(code[:-1]))
    return sum(complexity)


@timing
def part2(codes):
    
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        codes = [s.strip() for s in f.readlines()]
    print(part1(codes))
    print(part2(codes))
