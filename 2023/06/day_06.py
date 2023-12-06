#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from functools import reduce

def parse_races(races_str):
    races_str = races_str.split("\n")[:2]
    time = [int(d) for d in races_str[0][10:].split()] 
    distance = [int(d) for d in races_str[1][10:].split()]
    return [(time[i], distance[i]) for i in range(len(time))] 

def parse_races2(races_str):
    # single race -> concatenate the numbers
    races_str = races_str.split("\n")[:2]
    time = int(races_str[0][10:].replace(" ","")) 
    distance = int(races_str[1][10:].replace(" ",""))
    return (time, distance) 

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

def part2(race):
    record_beaten = 0
    for t in range(race[0]//2): # symmetrical -> can check for 1/2
        d = t * (race[0] - t)
        if d > race[1]:
            # for all values > t, we will beat the record
            record_beaten = (race[0] + 1) - t * 2
            break
    return record_beaten


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        races = parse_races(f.read())
    print("Part #1 :", part1(races))
    with open(input_file, 'r') as f:
        race = parse_races2(f.read())
    print("Part #2 :", part2(race))
