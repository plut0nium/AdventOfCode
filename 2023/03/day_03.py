#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

CHECK_POSITIONS = [(-1, -1), (-1, 0), (-1, 1),
                   ( 0, -1),          ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]
DIGITS = "1234567890"

def parse_schematic(sch_str):
    schematic = sch_str.split("\n")
    parts = []
    gears = defaultdict(list)
    for row, l in enumerate(schematic):
        pv = 0
        is_part_nr = False
        gear_at = set()
        for col, c in enumerate(l+"."): # add a . for end of line numbers
            if c in DIGITS:
                pv = pv * 10 + int(c)
                for d in CHECK_POSITIONS:
                    try:
                        if schematic[row + d[0]][col + d[1]] not in DIGITS+".":
                            is_part_nr = True
                        if schematic[row + d[0]][col + d[1]] == "*":
                            gear_at.add((row + d[0], col + d[1]))
                    except IndexError:
                        pass
            else:
                if pv > 0 and is_part_nr:
                    parts.append(pv)
                    if len(gear_at) > 0:
                        for g in gear_at:
                            gears[g].append(pv) 
                pv = 0
                is_part_nr = False
                gear_at.clear()
        # # handle part nr at end of line
        # if pv > 0 and is_part_nr:
        #     parts.append(pv)
        # pv = 0
        # is_part_nr = False
    return parts, gears

def part1(parts):
    return sum(parts)

def part2(gears):
    gear_ratio = 0
    for g, p in gears.items():
        if len(p) == 2:
            gear_ratio += p[0] * p[1]
    return gear_ratio
    

if __name__ == '__main__':
    with open(input_file, 'r') as f:
        parts, gears = parse_schematic(f.read())
    print("Part #1 :", part1(parts))
    print("Part #2 :", part2(gears))
