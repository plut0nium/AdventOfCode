#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from utils import timing

import re
from collections import deque

gate_re = re.compile(r'([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)')

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return a ^ b


@timing
def part1(gates, inputs):
    values = {k:v for k,v in inputs.items()}
    gates = deque(gates)
    while len(gates):
        g = gates.pop()
        if all(i in values for i in g[0]):
            values[g[2]] = g[1](*(values[i] for i in g[0]))
            continue
        gates.appendleft(g)
    return int("".join(map(str, (values[j] for j in reversed(sorted(values.keys())) if j.startswith("z")))), 2)


@timing
def part2(gates, inputs):

    return None


if __name__ == '__main__':
    inputs = {}
    gates = set()
    with open(input_file, 'r') as f:
        i_str, g_str = f.read().split("\n\n")
        for l in i_str.splitlines():
            k, v = l.strip().split(": ")
            inputs[k] = int(v)
        for g in gate_re.findall(g_str):
            if g[1] == "AND":
                op = AND
            elif g[1] == "OR":
                op = OR
            elif g[1] == "XOR":
                op = XOR
            else:
                raise ValueError(f"Unknown operation: {g[1]}")
            gates.add(((g[0], g[2]), op, g[3]))
    print(part1(gates, inputs))
    print(part2(gates, inputs))
