#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from time import time

coords_pattern = re.compile(r"x=(-?\d+), y=(-?\d+)")

input_file = "input"
Y = 2_000_000
search_area = ((0, 4_000_000), (0, 4_000_000))

# input_file = "test01.txt"
# Y = 10
# search_area = ((0, 20), (0, 20))

def dist_manhattan(a,b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def tuning_frequency(x, y):
    return x * 4_000_000 + y

def reduce_ranges(ranges):
    r = []
    for begin,end in sorted(ranges):
        if r and r[-1][1] >= begin - 1:
            r[-1][1] = max(r[-1][1], end)
        else:
            r.append([begin, end])
    return [tuple(c) for c in r]

def scan_y(sensors, y):
    covered = []
    for s, d in sensors.items():
        # distance between s and Y
        dy = abs(y - s[1])
        # width of the range at Y
        w = max(d - dy, 0)
        if w > 0:
            c = (s[0]-w, s[0]+w)
            #print(s, '->', c)
            covered.append(c)
    return reduce_ranges(covered)

if __name__ == '__main__':
    start_time = time()
    sensors = {}
    beacons = set()
    for l in open(input_file, 'r').readlines():
        s, b = [tuple(map(int, c)) for c in re.findall(coords_pattern, l)]
        sensors[s] = dist_manhattan(s, b)
        beacons.add(b)
    
    covered = scan_y(sensors, Y)
    p1 = sum(x2-x1+1 for x1,x2 in covered)
    p1 -= sum(1 for b in beacons if b[1]==Y)
    
    p2 = None
    for y in range(search_area[1][0], search_area[1][1]//2 + 1):
        y0 = search_area[1][1]//2
        for y1 in (y0 - y, y0 + y):
            c = scan_y(sensors, y1)
            if len(c) > 1:
                # we have a hole in the covered range
                x = c[0][1]+1
                if x in range(search_area[0][0], search_area[0][1]):
                    p2 = tuning_frequency(x, y1)
                    break
        if p2 is not None:
            break

    print("Part #1 :", p1)
    print("Part #2 :", p2)
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
