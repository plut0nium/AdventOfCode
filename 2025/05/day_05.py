#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test_01.txt"


def part1(available, fresh_list):
    fresh = set()
    for a in available:
        for f in fresh_list:
            if a in range(f[0], f[1]+1):
                fresh.add(a)
                break
    return len(fresh)


def part2(fresh_list):
    fresh_ranges = []
    for lo, hi in sorted(fresh_list):
        if fresh_ranges and fresh_ranges[-1][1] >= lo - 1:
            fresh_ranges[-1][1] = max(fresh_ranges[-1][1], hi)
        else:
            fresh_ranges.append([lo, hi])    
    return sum((hi - lo + 1) for lo, hi in fresh_ranges)


if __name__ == '__main__':

    with open(input_file, 'r') as f:
        fresh_list, available = (s.split() for s in f.read().split("\n\n"))
        fresh_list = [tuple(map(int, r.split("-"))) for r in fresh_list]
        available = list(map(int, available))   

    print(part1(available, fresh_list))
    print(part2(fresh_list))