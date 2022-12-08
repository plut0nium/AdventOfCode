#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

input_file = "input"
#input_file = "test01.txt"

def visibility(trees):
    x_max, y_max = trees.shape
    v = np.zeros((x_max, y_max), int)
    for y in range(y_max):
        for x in range(x_max):
            if x==0 or x==x_max-1 or y==0 or y==y_max-1:
                v[x, y] = 1
                continue
            h = trees[x,y]
            if h > max(trees[0:x,y]) or h > max(trees[x+1:x_max,y]):
                v[x, y] = 1
                continue                
            if h > max(trees[x,0:y]) or h > max(trees[x,y+1:y_max]):
                v[x, y] = 1
                continue
    return v

def score(trees):
    x_max, y_max = trees.shape
    s = np.zeros((x_max, y_max), int)
    for y in range(y_max):
        for x in range(x_max):
            if x==0 or x==x_max-1 or y==0 or y==y_max-1:
                # since (at least) one distance is zero, score is zero
                continue
            h = trees[x,y]
            directions = [np.flip(trees[0:x,y]),
                          trees[x+1:x_max,y],
                          np.flip(trees[x,0:y]),
                          trees[x,y+1:y_max] ]
            s[x,y] = math.prod((get_dist(h, d) for d in directions))
    return s

def get_dist(h, r):
    for i in range(len(r)):
        if r[i] >= h:
            break
    return i+1
    

if __name__ == '__main__':
    t = []
    for r in open(input_file, 'r').readlines():
        t.append([int(i) for i in r.strip()])
    trees = np.array(t)

    print("Part #1 :", np.count_nonzero(visibility(trees)))
    print("Part #2 :", np.max(score(trees)))
