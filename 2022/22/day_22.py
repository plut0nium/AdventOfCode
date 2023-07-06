#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
import re

input_file = "input"
# input_file = "test01.txt"

inst_pattern = re.compile(r'([RL]{1})')

dirs = [(0,1), (1,0), (0,-1), (-1,0)] # R, D, L, U

def cube_wrap(p, d, cx):
    x1, x2 = p
    if d % 2 == 1:
        x1, x2 = x2, x1
    nr = (x1 // cx) * cx - 1
    nc = x2 + sum(dirs[d]) * abs(x1 - nr)
    np1 = (nr, nc), sum(dirs[d]) * (d - 1) % 4
    nr = (x1 // cx + 1) * cx
    nc = x2 + sum(dirs[d]) * abs(x1 - nr)
    np2 = (nr, nc), sum(dirs[d]) * (d + 1) % 4
    nr = (((x1 // cx) + 2) % 4) * cx + cx - (x1 % cx + 1)
    np3 = (nr, x2 + cx), (d + 2) % 4
    np4 = (nr, x2 - cx), (d + 2) % 4
    np5 = (x1, (x2 + sum(dirs[d]) * 4 * cx)), d
    return [np1, np2, np3, np4, np5]

def monkey_map(board, inst, p=None, d=None, cube=False):
    if p is None:
        p = (0, min(b[1] for b in board.keys() if b[0]==0))
    if d is None:
        d = 0
    if cube:
        # get cube size
        rmax = max(b[0] for b in board.keys())
        cx = min(len([b for b in board.keys() if b[0]==r]) for r in [0, rmax])
    for i in inst:
        if i == 'R':
            d = (d + 1) % len(dirs)
        elif i == 'L':
            d = (d - 1) % len(dirs)
        else:
            for _ in range(i):
                np = (p[0] + dirs[d][0], p[1] + dirs[d][1])
                nd = d
                if np not in board:
                    # wrap around
                    if not cube: # Part 1
                        if d == 0:   # R
                            np = (p[0], min(b[1] for b in board.keys() if b[0]==p[0]))
                        elif d == 2: # L
                            np = (p[0], max(b[1] for b in board.keys() if b[0]==p[0]))
                        elif d == 1: # D
                            np = (min(b[0] for b in board.keys() if b[1]==p[1]), p[1])
                        elif d == 3: # U
                            np = (max(b[0] for b in board.keys() if b[1]==p[1]), p[1])
                        else:
                            raise ValueError("Unknown direction:", d)
                    else: # Part 2
                        for np_, nd_ in cube_wrap(p, d, cx):
                            print(p, d, cx, np_, nd_)
                            if d % 2 == 1:
                                np_ = np_[1], np_[0]
                            if np_ in board:
                                np = np_
                                nd = nd_
                                print("wrapping from ", p, d, "to", np, nd)
                                break
                if np not in board:
                    print("ERROR wrapping from ", p, d, "to", np)
                if board[np] == '#':
                    # stop moving
                    break
                else:
                    # move
                    p = np
                    if cube:
                        d = nd
    return p, d

def password(p, d):
    return (p[0] + 1) * 1000 + (p[1] + 1) * 4 + d


if __name__ == '__main__':
    start_time = time()
    board = {}
    with open(input_file, 'r') as f:
        board_raw, inst = f.read().split('\n\n')
    for i, r in enumerate(board_raw.splitlines()):
        for j, c in enumerate(r):
            if c in ['.', '#']:
                board[(i,j)] = c
            else:
                continue
    
    inst = [int(i) if i.isdigit() else i for i in inst_pattern.split(inst.strip())]
    
    p, d = monkey_map(board, inst)

    print("Part #1 :", password(p, d))
    
    p2, d2 = monkey_map(board, inst, cube=True)
    
    print("Part #2 :", password(p2, d2))
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
