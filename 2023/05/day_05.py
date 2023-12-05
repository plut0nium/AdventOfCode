#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
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

def get_location(s, almanac):
    # print("Seed: ", s)
    new_s = s
    for a in almanac:
        # loop through each map in the almanac
        for m in a:
            # check for each mapped range
            source, dest, length = m
            if new_s >= source and new_s < source + length:
                new_s = dest + (new_s - source)
                # print("> ", new_s, end=" ")
                break
            # if no range found, seed location is not updated
    # print() # newline
    return new_s

def part1(seeds, almanac):
    seed_location = []
    for s in seeds:
        seed_location.append(get_location(s, almanac))
    return min(seed_location)

def intersect(r1, r2):
    return (max(r1[0],r2[0]), min(r1[1],r2[1])) \
        if max(r1[0],r2[0]) <= min(r1[1],r2[1]) else None

def difference(r1, r2):
    # return r1 - r2
    if intersect(r1, r2) is None:
        return r1
    diff = []
    if r1[0] < r2[0]:
        diff.append((r1[0], r2[0] - 1))
    if r1[1] > r2[1]:
        diff.append((r2[1] + 1, r1[1]))
    return [d for d in diff]

def part2(seeds, almanac):
    # we have > 2E^10 seeds... let's avoid the brute force
    # print(sum((seeds[i]) for i in range(1, len(seeds), 2)))
    assert(len(seeds) % 2 == 0)
    seed_map = [(seeds[i], seeds[i] + seeds[i+1] - 1)
                    for i in range(0, len(seeds), 2)]

    for j, a in enumerate(almanac):
        # for each almanac "level"
        mapped_seeds = [] # seeds mapped to a new location
        for m in a:
            # ...for each mapped range
            source, dest, length = m
            r_min, r_max = source, source + length - 1
            r_move = dest - source
            # seeds
            not_mapped_seeds = [] # seeds that are not mapped (currently)
            for s in seed_map:
                s_min, s_max = s
                i = intersect((s_min, s_max), (r_min, r_max))
                if i is None:
                    # no intersection -> seeds are not moved
                    not_mapped_seeds.append((s_min, s_max))
                    continue
                # map seeds in range to new a location
                mapped_seeds.append((i[0] + r_move, i[1] + r_move))
                # keep remaining seeds (could be mapped by another range)
                not_mapped_seeds.extend(difference((s_min, s_max), (r_min, r_max)))
            # seeds can only be mapped by a single range at current almanac level
            seed_map = not_mapped_seeds
        seed_map = mapped_seeds + not_mapped_seeds
    return min((s[0] for s in seed_map))


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        seeds, almanac = parse_almanac(f.readlines())
    print("Part #1 :", part1(seeds, almanac))
    print("Part #2 :", part2(seeds, almanac))
