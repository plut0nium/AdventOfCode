#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

input_file = "input"
#input_file = "test01.txt"

def view_and_score(trees):
    x_max, y_max = trees.shape
    v = np.zeros((x_max, y_max), int)
    s = np.zeros((x_max, y_max), int)
    for y in range(y_max):
        for x in range(x_max):
            if x==0 or x==x_max-1 or y==0 or y==y_max-1:
                # edge cases
                v[x, y] = 1
                # since (at least) one distance is zero, score stays zero
                continue
            h = trees[x,y]
            views = [np.flip(trees[:x,y]),
                     trees[x+1:,y],
                     np.flip(trees[x,:y]),
                     trees[x,y+1:] ]
            if any((h > max(v) for v in views)):
                # tree is visible from edge
                v[x, y] = 1
            s[x,y] = math.prod((sight_distance(h, d) for d in views))
    return v, s

def sight_distance(h, r):
    for i in range(len(r)):
        if r[i] >= h:
            break
    return i+1
    

if __name__ == '__main__':
    t = []
    for r in open(input_file, 'r').readlines():
        t.append([int(i) for i in r.strip()])
    trees = np.array(t)

    v, s = view_and_score(trees)

    print("Part #1 :", np.count_nonzero(v))
    print("Part #2 :", np.max(s))
