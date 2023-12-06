#!/usr/bin/env python
# -*- coding: utf-8 -*-

from grid import Grid
from collections import deque

input_file = "input18.txt"

def reachablekeys(grid, start, havekeys):
    bfs = deque([start])
    distance = {start: 0}
    keys = {}
    while bfs:
        h = bfs.popleft()
        for pt in [
            (h[0] + 1, h[1]),
            (h[0] - 1, h[1]),
            (h[0], h[1] + 1),
            (h[0], h[1] - 1),
        ]:
            if not grid.is_in(pt[0], pt[1]):
                continue
            ch = grid.get(pt[0], pt[1])
            if ch == '#':
                continue
            if pt in distance:
                continue
            distance[pt] = distance[h] + 1
            if ch.isupper() and ch.lower() not in havekeys:
                continue
            if ch.islower() and ch not in havekeys:
                keys[ch] = distance[pt], pt
            else:
                bfs.append(pt)
    return keys

def reachable4(grid, starts, havekeys):
    keys = {}
    for i, start in enumerate(starts):
        for ch, (dist, pt) in reachablekeys(grid, start, havekeys).items():
            keys[ch] = dist, pt, i
    return keys

seen = {}
def minwalk(grid, start, havekeys):
    hks = ''.join(sorted(havekeys))
    if (start, hks) in seen:
        return seen[start, hks]
    # if len(seen) % 10 == 0:
    #     print(hks)
    keys = reachablekeys(grid, start, havekeys)
    if len(keys) == 0:
        # done!
        ans = 0
    else:
        poss = []
        for ch, (dist, pt) in keys.items():
            poss.append(dist + minwalk(grid, pt, havekeys + ch))
        ans = min(poss)
    seen[start, hks] = ans
    return ans

def minwalk4(grid, starts, havekeys):
    hks = ''.join(sorted(havekeys))
    if (starts, hks) in seen:
        return seen[starts, hks]
    # if len(seen) % 10 == 0:
    #     print(hks)
    keys = reachable4(grid, starts, havekeys)
    if len(keys) == 0:
        # done!
        ans = 0
    else:
        poss = []
        for ch, (dist, pt, roi) in keys.items():
            nstarts = tuple(pt if i == roi else p for i, p in enumerate(starts))
            poss.append(dist + minwalk4(grid, nstarts, havekeys + ch))
        ans = min(poss)
    seen[starts, hks] = ans
    return ans


if __name__ == '__main__':
    maze = Grid('.')
    x,y = 0,0
    keys = {}
    doors = {}
    with open(input_file, 'r') as f:
        for l in f.readlines():
            for m in l.strip():
                maze.set(x,y,m)
                if m == '@':
                    start_position = (x,y)
                x += 1
            y += 1
            x = 0
    # set origin at @
    maze.set_origin(start_position[0],start_position[1])
    print("Part 1:", minwalk(maze, (0,0), ''))
    
    maze.set(-1,-1, '@')
    maze.set(-1, 1, '@')
    maze.set( 1,-1, '@')
    maze.set( 1, 1, '@')
    maze.set( 0, 0, '#')
    maze.set(-1, 0, '#')
    maze.set( 1, 0, '#')
    maze.set( 0,-1, '#')
    maze.set( 0, 1, '#')
    starts = tuple([(-1,-1),(-1,1),(1,-1),(1,1)])
    seen = {}
    print("Part 2:", minwalk4(maze, starts, ''))

    
