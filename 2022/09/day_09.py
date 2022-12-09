#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
#input_file = "test01.txt"
#input_file = "test02.txt"

grid = defaultdict(int)
grid2 = defaultdict(int)

directions = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

def move_tail(h, t):
    hx, hy = h
    tx, ty = t
    if abs(hx-tx) <= 1 and abs(hy-ty) <= 1:
        m = (0,0)
    elif hx==tx or hy==ty:
        # on the same row/col
        m = ((hx-tx)//2, (hy-ty)//2)
    else:        
        m = (int((hx-tx)/abs(hx-tx)), int((hy-ty)/abs(hy-ty)))
    return tuple(map(lambda x, y: x + y, t, m))

if __name__ == '__main__':
    moves = []
    for l in open(input_file, 'r').readlines():
        d, n = l.strip().split()
        moves.append((d, int(n)))
    rope = [(0,0), (0,0)]
    rope2 = [(0,0) for _ in range(10)]

    for m in moves:
        d,n = m
        for i in range(n):
            # move Head
            rope[0] = tuple(map(lambda x, y: x + y, rope[0], directions[d]))
            rope2[0] = tuple(map(lambda x, y: x + y, rope2[0], directions[d]))
            # move Tail
            rope[1] = move_tail(rope[0], rope[1])
            for i in range(1,len(rope2)):
                rope2[i] = move_tail(rope2[i-1], rope2[i])
            grid[rope[1]] += 1
            grid2[rope2[-1]] += 1

    print("Part #1 :", len(grid))
    print("Part #2 :", len(grid2))
