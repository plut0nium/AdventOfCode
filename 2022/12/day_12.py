#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

input_file = "input"
#input_file = "test01.txt"

START = ord('S')
END = ord('E')

moves = ((1, 0), (-1, 0), (0, -1), (0, 1))

def hill_climbing_algorithm(start_coord, height_map):
    """ More a Hill Descending Algorithm """
    visited = {}
    candidate = [(start_coord, 0)]
    while len(candidate):
        current, steps = candidate.pop()
        for m in moves:
            dest = (current[0]+m[0], current[1]+m[1])
            if -1 in dest \
                or dest[0] >= height_map.shape[0] \
                or dest[1] >= height_map.shape[1]:
                # out of map
                continue
            if height_map[dest] < height_map[current]-1:
                # cannot climb if step > 1 in the ascending direction
                continue
            if dest not in visited or visited[dest] > steps+1:
                candidate.append((dest, steps+1))
        visited[current] = steps
    return visited

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

    # start from the top
    # allows for easily solving parts 1 & 2
    visited = hill_climbing_algorithm(end_coord, height_map)
    
    # potential starting points
    s = np.where(height_map == ord('a'))
    starting_points = list(zip(s[0], s[1]))

    print("Part #1 :", visited[start_coord])
    print("Part #2 :", min((visited[s] for s in starting_points if s in visited)))
