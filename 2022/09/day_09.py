#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
#input_file = "test01.txt"
#input_file = "test02.txt"

directions = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

def rope_bridge(length, moves):
    grid = defaultdict(int)
    rope = [(0,0) for _ in range(length)]
    for m in moves:
        d,n = m
        for i in range(n):
            # move Head
            rope[0] = tuple(map(lambda x, y: x + y, rope[0], directions[d]))
            # move Tail
            for i in range(1,len(rope)):
                rope[i] = move_tail(rope[i-1], rope[i])
            grid[rope[-1]] += 1
    return len(grid)

def move_tail(h, t):
    hx, hy = h
    tx, ty = t
    if abs(hx-tx) <= 1 and abs(hy-ty) <= 1:
        # touching, dont move
        return t
    dx, dy = (0,0)
    if hx != tx:
        dx = int((hx-tx)/abs(hx-tx))
    if hy != ty:
        dy = int((hy-ty)/abs(hy-ty))
    return tuple(map(lambda x, y: x + y, t, (dx, dy)))

if __name__ == '__main__':
    moves = []
    for l in open(input_file, 'r').readlines():
        d, n = l.strip().split()
        moves.append((d, int(n)))

    print("Part #1 :", rope_bridge(2, moves))
    print("Part #2 :", rope_bridge(10, moves))
