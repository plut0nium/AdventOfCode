#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

input_file = "input"
#input_file = "test01.txt"

START = ord('S')
END = ord('E')

move = ((1, 0), (-1, 0), (0, -1), (0, 1))

if __name__ == '__main__':
    with open(input_file, 'r') as f:
        m = [[ord(h) for h in l] for l in f.read().strip().split('\n')]

    for r in range(len(m)):
        if START in m[r]:
            start_coord = (r, m[r].index(START))
        if END in m[r]:
            end_coord = (r, m[r].index(END))
            
    height_map = np.array(m)
    height_map[start_coord] = ord('a')
    height_map[end_coord] = ord('z')
    visited = {}
    candidate = [(start_coord, 0)]

    while len(candidate):
        current, steps = candidate.pop()
        for n in move:
            dest = (current[0]+n[0], current[1]+n[1])
            if -1 in dest \
                or dest[0] >= height_map.shape[0] \
                or dest[1] >= height_map.shape[1]:
                # out of map
                continue
            if height_map[dest] > height_map[current]+1:
                # cannot climb
                continue
            if dest not in visited or visited[dest] > steps+1:
                candidate.append((dest, steps+1))
        visited[current] = steps
    
    start_coord = end_coord
    candidate = [(start_coord, 0)]
    visited2 = {}

    while len(candidate):
        current, steps = candidate.pop()
        for n in move:
            dest = (current[0]+n[0], current[1]+n[1])
            if -1 in dest \
                or dest[0] >= height_map.shape[0] \
                or dest[1] >= height_map.shape[1]:
                # out of map
                continue
            if height_map[dest] < height_map[current]-1:
                # cannot climb
                continue
            if dest not in visited2 or visited2[dest] > steps+1:
                candidate.append((dest, steps+1))
        visited2[current] = steps
    
    s = np.where(height_map == ord('a'))
    ss = list(zip(s[0], s[1]))

    print("Part #1 :", visited[end_coord])
    print("Part #2 :", min((visited2[s] for s in ss if s in visited2)))
