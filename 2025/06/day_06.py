#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test_01.txt"

from math import prod

def part1(problems):
    total = 0
    for p in problems:
        op = p.pop()
        if op == '+':
            total += sum(p)
        elif op =='*':
            total += prod(p)
        else:
            raise ValueError("Unknown operation")
    return total


def part2(problems):

    return part1(problems)


if __name__ == '__main__':
    problems = []
    with open(input_file, 'r') as f:
        for l in f.readlines():
            for i, v in enumerate(l.split()):
                if i > (len(problems) - 1):
                    problems.append([])
                try:
                    v = int(v)
                except ValueError:
                    pass
                problems[i].append(v)
    
    print(part1(problems))
    
    problems_str = []
    with open(input_file, 'r') as f:
        for l in f.readlines():
            if len(l):
                problems_str.append(l)
    # rotate 90° anti-clockwise (all lines have the same length)
    problems_str = list(''.join(x) for x in zip(*problems_str))[::-1]
    problems2 = [[]]
    for p in problems_str:
        p = p.strip()
        if len(p) == 0:
            if len(problems2[-1]) == 0:
                pass
            else:
                problems2.append([])
            continue
        if p[-1].isdecimal():
            problems2[-1].append(int(p))
        else:
            problems2[-1].append(int(p[:-1]))
            problems2[-1].append(p[-1])
    
    print(part2(problems2))