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
from itertools import permutations, batched, chain
from random import randrange

MAX_BITS = int("1" * 45, 2)

gate_re = re.compile(r'([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)')

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return a ^ b

def find_gate_by_input(gates, *inputs):
    found = []
    for g in gates:
        if all(i in g[0] for i in inputs):
            found.append(g)
    if len(found):
        return found
    return None

def find_gate_by_output(gates, output):
    found = []
    for g in gates:
        if g[2] == output:
            found.append(g)
    if len(found):
        return found
    return None

def find_gate_by_type(gates, gtype):
    found = []
    for g in gates:
        if g[1] == gtype:
            found.add(g)
    if len(found):
        return found
    return None

def count_gates(gates, gtype=None):
    if gtype:
        return len([g for g in gates if g[1] == gtype])
    return len(gates)

def swap_gates(gates, swap):
    gates = list(gates)[:]
    for i, g in enumerate(gates):
        if g[2] not in tuple(chain(*swap)):
            continue
        for s in swap:
            a, b = s
            if g[2] == a:
                gates[i] = (g[0], g[1], b)
            elif g[2] == b:
                gates[i] = (g[0], g[1], a)
    return set(gates)

def run(gates, inputs):
    values = {k:v for k,v in inputs.items()}
    gates = deque(gates)
    while len(gates):
        g = gates.pop()
        if all(i in values for i in g[0]):
            values[g[2]] = g[1](*(values[i] for i in g[0]))
            continue
        gates.appendleft(g)
    return int("".join(map(str, (values[j] for j in reversed(sorted(values.keys())) \
                                           if j.startswith("z")))),
               base= 2)

@timing
def part1(gates, inputs):
    return run(gates, inputs)


@timing
def part2(gates, inputs):
    if "test" in input_file:
        # only works on full input
        return None
    swap_candidates = set()
    
    internal_signals = set(g[2] for g in gates if not (g[2].startswith(("x", "y", "z"))))
    for s in internal_signals:
        if not any(s in g[0] for g in gates):
            swap_candidates.add(s)

    for g in gates:
        if g[1] != XOR and g[2].startswith("z") and g[2] not in internal_signals:
            # output bits should come from an XOR gate, except z45
            if g[2] != "z45":
                swap_candidates.add(g[2])
                # print(g)
                # continue
        for s in g[0]:
            if s.startswith("z") and s not in internal_signals:
                swap_candidates.add(s)
                pass
        
        if g[1] == OR:
            for s in g[0]:
                if len(h := find_gate_by_output(gates, s)) != 1:
                    raise ValueError(f"Should be only 1 gate with output = {s}")
                if h[0][1] != AND:
                    # OR gates should take their input from AND gates
                    swap_candidates.add(h[0][2])
                    # print(h[0])
            if g[2] == "z45":
                # last output bit goes nowhere
                continue
            gx = find_gate_by_input(gates, g[2])
            if gx is None:
                swap_candidates.add(g[2])
                # print(g)
                continue
            # carry-out must go into 1x AND and 1x XOR
            assert len(gx) == 2
            assert count_gates(gx, XOR) == 1 \
                   and count_gates(gx, AND) == 1
            # todo

    # according to puzzle description, input gates are OK
    # only output wires can be swapped
    
    for i in range(len(inputs) // 2): # 0..44
        x = f"x{i:02}"
        y = f"y{i:02}"
        gx = find_gate_by_input(gates, x, y)
        assert count_gates(gx, XOR) == 1 \
               and count_gates(gx, AND) == 1
        for g in gx:
            if g[1] == XOR:
                # 1st level XOR
                if i == 0:
                    if g[2] != "z00":
                        swap_candidates.add(g[2])
                        swap_candidates.add("z00")
                    continue
                if g[2].startswith("z")  and g[2] not in internal_signals:
                    swap_candidates.add(g[2])
                    # print(g)
                hx = find_gate_by_input(gates, g[2])
                if hx is None:
                    swap_candidates.add(g[2])
                    # print(g)
                    continue
                elif len(hx) != 2:
                    swap_candidates.add(g[2])
                    # print(hx)
                    continue
                assert count_gates(hx, XOR) == 1 \
                       and count_gates(hx, AND) == 1
                for h in hx:
                    if h[1] == XOR and not h[2].startswith("z"):
                        swap_candidates.add(h[2])
                        # print(h)
                        continue
            elif g[1] == AND:
                # 1st level AND
                hx = find_gate_by_input(gates, g[2])
                if hx is not None:
                    if i == 0 and len(hx) == 2:
                        pass
                    elif len(hx) != 1:
                        swap_candidates.add(g[2])
            else:
                raise ValueError(f"Incorrect gate type: {g[1]}")

    assert len(swap_candidates) == 8

    # # generate 10 tests
    # tests = []
    # for j in range(10):
    #     test_input = {}
    #     a, b = (randrange(MAX_BITS + 1) for _ in range(2))
    #     c = a + b
    #     for k in range(45):
    #         test_input[f"x{k:02}"] = (a >> k) & 1
    #         test_input[f"y{k:02}"] = (b >> k) & 1
    #     tests.append((test_input, c))

    # for p in permutations(swap_candidates):
    #     # not efficent, still testing 40k+ combinations
    #     swap = tuple(batched(p, 2))
    #     swapped = swap_gates(gates, swap)
    #     print(swapped.difference(gates))
    #     if any(run(swapped, t[0]) != t[1] for t in tests):
    #         continue
    #     print("Test succeeded: ", p)

    # return len(swap_candidates)
    return ",".join(sorted(swap_candidates))


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
