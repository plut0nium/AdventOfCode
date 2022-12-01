#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test1.txt"

from math import sqrt

def reaches_target(v):
    p = [0, 0]
    while True:
        for i in range(2):
            p[i] += v[i]
        v[0] -= 1 if v[0] else 0
        v[1] -= 1
        if p[0] > t_max[0] or p[1] < t_min[1]:
            return False
        if all((t_min[i] <= p[i] <= t_max[i] for i in range(2))):
            return True

if __name__ == '__main__':
    for l in open(input_file).readlines():
        # target = [int(i) for i in findall(r'-?\d+', l.strip())]
        target = tuple(tuple(int(i) for i in a.split("=")[1].split("..")) for a in l.strip().split(","))

        y_min = target[1][0]
        y = -y_min - 1
        print(int(y * (y + 1) / 2))

        t_min = tuple(b[0] for b in target)
        t_max = tuple(b[1] for b in target)
        v0_min = (int(sqrt(t_min[0] * 2)), t_min[1])
        v0_max = (t_max[0], abs(t_min[1] + 1))
        
        r2 = 0
        for v0_x in range(v0_min[0], v0_max[0] + 1):
            for v0_y in range(v0_min[1], v0_max[1] + 1):
                r2 += reaches_target([v0_x, v0_y])
        
        print(r2)
