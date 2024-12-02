#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"

from copy import copy

def check_report(r):
    diff = [r[i] - r[i-1] for i in range(1, len(r))]
    if not all(d >= 0 for d in diff) and not all(d<=0 for d in diff):
        # r is unsafe (not all increasing/decreasing)
        return False
    if all(abs(d) >= 1 and abs(d)<=3 for d in diff):
        # r is safe (variations within [1,3] range)
        return True
    return False


def part1(reports):
    c= 0
    for r in reports:
        if check_report(r):
            c += 1
    return c


def part2(reports):
    c= 0
    for r in reports:
        if check_report(r):
            c += 1
            continue # record is safe as-is
        for i in range(len(r)):
            _r = copy(r)
            del _r[i] # remove 1 record level
            if check_report(_r):
                c += 1
                break            
    return c


if __name__ == '__main__':
    reports = []
    for l in open(input_file, 'r').readlines():
        reports.append(list(map(int, l.strip().split())))
    print(part1(reports))
    print(part2(reports))
