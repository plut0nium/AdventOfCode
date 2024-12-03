#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from functools import reduce
import math

def parse_races(races_str):
    races_str = races_str.split("\n")[:2]
    time = [int(d) for d in races_str[0][10:].split()] 
    distance = [int(d) for d in races_str[1][10:].split()]
    return [(time[i], distance[i]) for i in range(len(time))] 

def part1(races):
    record_beaten = [0 for _ in races]
    for i, r in enumerate(races):
        # print("Race ", r)
        for t in range(r[0]+1):
            d = t * (r[0] - t)
            # print("Hold:", t, "->", "Distance", d)
            if d > r[1]:
                record_beaten[i] += 1
    return reduce(lambda x, y: x*y, record_beaten)

def part2(race, brute=False):
    if brute:
        record_beaten = 0
        for t in range(race[0]//2): # symmetrical -> can check for 1/2
            d = t * (race[0] - t)
            if d > race[1]:
                # for all values > t, we will beat the record
                record_beaten = (race[0] + 1) - t * 2
                break
    else:
        # this equals to solve (find the roots of)
        # the following quadratic equation
        #   t ** 2 - t * race[0] + race[1] = 0
        delta = race[0] ** 2 - 4 * race[1]
        t1 = (race[0] - math.sqrt(delta)) / 2
        t2 = (race[0] + math.sqrt(delta)) / 2
        # assume t2 > t1
        if t1.is_integer(): # this value will match the record but not beat it...
            t1 += 1
        if t2.is_integer():
            t2 -= 1
        record_beaten = math.floor(t2) - math.ceil(t1) + 1
    return record_beaten


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        races = parse_races(f.read())
    print("Part #1 :", part1(races))
    race = tuple((reduce(lambda x,y: x * 10 ** int(math.log10(y) + 1) + y , z)
                  for z in zip(*races)))
    print("Part #2 :", part2(race))
