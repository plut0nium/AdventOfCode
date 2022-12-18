#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from copy import deepcopy

input_file = "input"
# input_file = "test01.txt"

origin = (0,0,0)
dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

def manhattan(a, b):
    # manhattan distance between a & b
    return sum(map(lambda c: abs(c[0]-c[1]), zip(a, b)))

def dist(a,b):
    # Euclidean distance
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) ** 0.5

def steam_path(a, b, droplet, visited=None):
    # A* - return length of path from a to b
    if visited is None:
        visited = set()
    visited.add(a)
    adj = [tuple(map(sum, zip(a, d))) for d in dirs]
    if b in adj:
        # b is directly reachable
        return 1
    candidate = [(a, manhattan(a, origin)) for a in adj]
    for n, d in sorted(candidate, key=lambda a: a[1]):
        if n in droplet:
            # solid cube
            continue
        if n in visited:
            # already checked
            continue
        p = steam_path(n, b, droplet, visited)
        if p is not None:
            return (p + 1)
    return None

if __name__ == '__main__':
    start_time = time()
    
    cubes = dict.fromkeys([tuple(map(int, l.strip().split(',')))
                           for l in open(input_file, 'r').readlines()], None)

    pockets = set()
    for xyz in cubes.keys():
        if cubes[xyz] is None:
            cubes[xyz] = list(0 for _ in range(2))
        for d in dirs:
            adj = tuple(map(sum, zip(xyz, d)))
            if adj in cubes:
                # solid adjacent cube
                cubes[xyz][0] += 1
            # part 1 ends here...
            else:
                # check if pocket
                #print("checking pocket", adj)
                if adj in pockets:
                    cubes[xyz][1] += 1
                else:
                    # we assume origin is outside of droplet
                    s = steam_path(adj, origin, cubes)
                    if s is None:
                        pockets.add(adj)
                        cubes[xyz][1] += 1
    
    print("Part #1 :", len(cubes) * 6 - sum(v[0] for v in cubes.values()))
    
    print("Part #2 :", len(cubes) * 6 - sum(v[0] for v in cubes.values()) \
                                      - sum(v[1] for v in cubes.values()))
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
