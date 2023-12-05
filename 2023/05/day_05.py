#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
input_file = "test01.txt"
# input_file = "test02.txt"

def parse_almanac(almanac_list):
    seeds = [int(s) for s in almanac_list.pop(0)[7:].split()]
    maps = []
    current_map = []
    for l in almanac_list:
        if len(l.strip()) == 0:
            # empty line
            pass
        elif l.strip().endswith("map:"):
            # start a new map
            if len(current_map):
                maps.append(current_map)
            current_map = []
        else:
            dest, source, length =  (int(i) for i in l.strip().split())
            current_map.append((source, dest, length))
    if len(current_map):
        maps.append(current_map)
    return seeds, maps

def get_position(s, almanac):
    # print("Seed: ", s)
    new_s = s
    for a in almanac:
        for m in a:
            source, dest, length = m
            if new_s >= source and new_s < source + length:
                new_s = dest + (new_s - source)
                # print("> ", new_s, end=" ")
                break
    # print("")
    return new_s
        

def part1(seeds, almanac):
    seed_position = []
    for s in seeds:
        seed_position.append(get_position(s, almanac))
    return min(seed_position)
    
def part2(cards):
    return None


if __name__ == '__main__':
    almanac = None
    with open(input_file, 'r') as f:
        seeds, almanac = parse_almanac(f.readlines())
    print("Part #1 :", part1(seeds, almanac))
    print("Part #2 :", part2(almanac))
