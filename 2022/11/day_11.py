#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

import math
from copy import deepcopy

ROUNDS = 20
ROUNDS2 = 10_000

class Monkey:
    def __init__(self, i, o, t, dt, df):
        self.items = i
        self.op = o
        self.test = t
        self.dest_true = dt
        self.dest_false = df
        self.count = 0

def parse_monkey(m):
    m = m.split('\n')
    items = [int(i) for i in m[1][18:].split(', ')]
    if m[2][23] == '+':
        o1 = sum
    elif m[2][23] == '*':
        o1 = math.prod
    else:
        print('Error - Unknown operation')
    if m[2][25:] == 'old':
        o2 = 'old'
    else:
        o2 = int(m[2][25:])
    op = (o1, o2)
    test = int(m[3][21:])
    dest_true = int(m[4][29:])
    dest_false = int(m[5][30:])
    return Monkey(items, op, test, dest_true, dest_false)

if __name__ == '__main__':
    monkeys = []
    with open(input_file, 'r') as f:
        m = f.read().strip().split('\n\n')
    for m_ in m:
        monkeys.append(parse_monkey(m_))
        
    monkeys2 = deepcopy(monkeys)

    # part 1
    for r in range(ROUNDS):
        for m in monkeys:
            for i in m.items:
                i = m.op[0]((i, i if m.op[1]=='old' else m.op[1]))
                i = i//3
                if i % m.test == 0:
                    monkeys[m.dest_true].items.append(i)
                else:
                    monkeys[m.dest_false].items.append(i)
                m.count += 1
            m.items = []

    c = sorted([m.count for m in monkeys])

    # part 2
    d = math.prod((m.test for m in monkeys2))
    for r in range(ROUNDS2):
        for m in monkeys2:
            for i in m.items:
                i = m.op[0]((i, i if m.op[1]=='old' else m.op[1]))
                #i = i//3
                i = i % d
                if i % m.test == 0:
                    monkeys2[m.dest_true].items.append(i)
                else:
                    monkeys2[m.dest_false].items.append(i)
                m.count += 1
            m.items = []

    c2 = sorted([m.count for m in monkeys2])
    
    print("Part #1 :", math.prod(c[-2:]))
    print("Part #2 :", math.prod(c2[-2:]))
