#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

if __name__ == '__main__':
    overlap = 0
    included = 0
    for l in open(input_file).readlines():
        c1,c2 = [[int(x) for x in p.split('-')]
                     for p in l.strip().split(',')] 
        if ((c1[0] <= c2[0]) and (c1[1] >= c2[1])) \
            or ((c2[0] <= c1[0]) and (c2[1] >= c1[1])):
                included += 1
        if max(c1[0], c2[0]) <= min(c1[1], c2[1]):
            overlap += 1
    print("Part #1 :", included)
    print("Part #2 :", overlap)
