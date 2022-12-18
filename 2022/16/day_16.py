#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from time import time
from copy import copy

input_file = "input"
input_file = "test01.txt"

valve_pattern = re.compile(r"([A-Z]{2})")
flow_pattern = re.compile(r"(\d+)")

TIMEOUT = 30
start = "AA"

def find_path(a, b, cave, visited, max_length):
    # return the shortest path from a to b
    visited.append(a)
    if b in cave[a][1]:
        # b is directly reachable
        return 1
    elif max_length == 1:
        # cannot reach b
        return None
    paths = []
    for n in cave[a][1]:
        if n in visited:
            # we already went trough this node
            continue
        p = find_path(n, b, cave, copy(visited), max_length-1)
        if p is not None:
            paths.append(p)
    if len(paths):
        return min(paths) + 1
    return None


if __name__ == '__main__':
    start_time = time()
    cave = {}
    for l in open(input_file, 'r').readlines():
        valve, *tunnels = re.findall(valve_pattern, l)
        flow = int(re.findall(flow_pattern, l)[0])
        cave[valve] = (flow, tunnels)

    useful = [(v, f[0]) for v, f in cave.items() if f[0] > 0]

    released = 0
    t = TIMEOUT
    current = start
    while len(useful) and t >= 0:
        print(current, t)
        c = [] # candidates
        for u in useful:
            # time to reach (& open)
            ttr = find_path(current, u[0], cave, [], t) + 1
            if ttr >= t:
                # not enough time
                continue
            # how much pressure can we release
            # flow * remaining_time
            r = u[1] * (t - ttr)
            c.append((u, r, ttr))
            print(">", u[0], ttr, r)
        if not len(c):
            # no time to do anything
            break
        # sort by released pressure & select highest
        n = sorted(c, key=lambda x: x[1])[-1]
        current = n[0][0]
        released += n[1]
        t -= n[2]
        useful.remove(n[0])

    print("Part #1 :", released)
    print("Part #2 :", None)
    
    #print("Execution time: {:.6f}s".format((time() - start_time)))
