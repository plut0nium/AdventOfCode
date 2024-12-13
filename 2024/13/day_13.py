#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"


from collections import defaultdict, Counter
import re
import numpy as np

machine_regex = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\n'
                          +r'Button B: X\+(\d+), Y\+(\d+)\n'
                          +r'Prize: X=(\d+), Y=(\d+)')
TARGET_OFFSET = 10000000000000

def part1(machines):
    token_count = 0
    for m in machines:
        A, B, target = m
        a = np.array([[A[0], B[0]], [A[1], B[1]]]) # could transpose
        b = np.array(target)
        sol = np.around(np.linalg.solve(a, b), 3)
        if all(x.is_integer() for x in sol):
            token_count += int(3 * sol[0] + 1 * sol[1])
    return token_count


def part2(machines):
    token_count = 0
    for m in machines:
        A, B, target = m
        a = np.array([[A[0], B[0]], [A[1], B[1]]]) # could transpose
        b = np.array(target) + TARGET_OFFSET
        sol = np.around(np.linalg.solve(a, b), 3)
        if all(x.is_integer() for x in sol):
            token_count += int(3 * sol[0] + 1 * sol[1])
    return token_count


if __name__ == '__main__':
    machines = []
    with open(input_file, 'r') as f:
        for m in f.read().split("\n\n"):
            ax, ay, bx, by, tx, ty = map(int, machine_regex.match(m).groups())
            machines.append(((ax, ay), (bx, by), (tx, ty)))
    print(part1(machines))
    print(part2(machines))
