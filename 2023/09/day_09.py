#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

def parse_report(report_lines):
    report = []
    for r in report_lines:
        report.append([int(g) for g in r.strip().split()])
    return report

def extrapolate(history):
    steps = []
    steps.append(history)
    while any((v !=0 for v in steps[-1])):
        # we could also check if all values are identical
        # this would save 1 step...
        steps.append(diff(steps[-1]))
    # for s in steps:
    #     print(s)
    for i in reversed(range(len(steps))):
        if i == len(steps) - 1:
            steps[i].append(0)
            continue
        steps[i].append(steps[i][-1] + steps[i+1][-1])
    return steps[0][-1]

def diff(history):
    return [history[i+1] - history[i] for i in range(len(history) - 1)]

def part1(report):
    return sum([extrapolate(history) for history in report])

def part2(report):
    return sum([extrapolate(list(reversed(history))) for history in report])


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        report = parse_report(f.readlines())
    print("Part #1 :", part1(report))
    print("Part #2 :", part2(report))
