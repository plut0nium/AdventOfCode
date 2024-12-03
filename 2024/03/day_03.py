#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from copy import copy
import re

mul_re = re.compile(r'mul\(\d+,\d+\)')
mul_re_part2 = re.compile(r'(?:mul\(\d+,\d+\))|(?:do\(\))|(?:don\'t\(\))')


def part1(program):
    result = 0
    valid = mul_re.findall(program)
    for v in valid:
        x, y = list(map(int, v[4:-1].split(',')))
        result += x * y
    return result


def part2(program):
    result = 0
    enabled = True
    valid = mul_re_part2.findall(program)
    for v in valid:
        if v == "do()":
            enabled = True
        elif v == "don't()":
            enabled = False
        else:
            if enabled:
                x, y = list(map(int, v[4:-1].split(',')))
                result += x * y
    return result


if __name__ == '__main__':
    with open(input_file, 'r') as file:
        program = file.read()
    print(part1(program))
    print(part2(program))
