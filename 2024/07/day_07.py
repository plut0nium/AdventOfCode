#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from math import log10, ceil
from itertools import product

OPERATORS = ["+", "*", "||"]


def check_equations(equations, operators):
    valid = []
    for e in equations:
        value = e[0]
        numbers = e[1]
        for ops in product(operators, repeat=(len(numbers) - 1)):
            result = numbers[0]
            for i, o in enumerate(ops):
                if o == "+":
                    result += numbers[i+1]
                elif o == "*":
                    result *= numbers[i+1]
                elif o == "||":
                    # result *= 10**ceil(log10(numbers[i+1]))
                    # result += numbers[i+1]
                    result = int(f"{result}{numbers[i+1]}")
                else:
                    raise ValueError(f"Unknown operator: {o}")
            if result == value:
                valid.append(e)
                break
    return valid


def part1(equations):
    return sum(e[0] for e in check_equations(equations, OPERATORS[:2]))


def part2(equations):
    v1 = check_equations(equations, OPERATORS[:2])
    v2 = check_equations([e for e in equations if e not in v1], OPERATORS)
    return sum(e[0] for e in v1 + v2)


if __name__ == '__main__':
    equations = []
    with open(input_file, 'r') as f:
        for e_str in f.readlines():
            value, num_str = e_str.split(": ")
            numbers = tuple(map(int, num_str.strip().split(" ")))
            equations.append((int(value), numbers))
    print(part1(equations))
    print(part2(equations))
