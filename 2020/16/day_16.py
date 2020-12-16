#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from itertools import product

input_file = "input"
# input_file = "test1.txt"
# input_file = "test2.txt" 

re_rule = re.compile(r'^([\w ]+)\: (\d+)-(\d+) or (\d+)-(\d+)')

RULE, MY_TICKET, TICKET = range(3)

if __name__ == '__main__':
    count1, count2 = 0, 0

    rules = {}
    tickets = []
    my_ticket = None

    with open(input_file,'r') as f:
        line_type = RULE
        for l in f.readlines():
            if not l.strip():
                continue
            if l.startswith("your ticket:"):
                line_type = MY_TICKET
            elif l.startswith("nearby tickets:"):
                line_type = TICKET
            else:
                if line_type == RULE:
                    r = re_rule.match(l.strip()).groups()
                    rules[r[0]] = [range(int(r[1]),int(r[2])+1), range(int(r[3]),int(r[4])+1)]
                elif line_type == MY_TICKET:
                    my_ticket = [int(i) for i in l.strip().split(',')]
                else:
                    tickets.append([int(i) for i in l.strip().split(',')])
    
    # part 1
    all_rules = [r for rs in rules.values() for r in rs]
    invalid = set()
    for i,t in enumerate(tickets):
        for v in t:
            if not any(v in r for r in all_rules):
                count1 += v
                invalid.add(i)
    
    # part 2
    fields_candidate = [set(rules.keys()) for i in range(len(my_ticket))]
    for i,t in enumerate(tickets):
        if i in invalid:
            continue
        for j,f in enumerate(fields_candidate):
            to_remove = []
            for r in f:
                if t[j] not in rules[r][0] and t[j] not in rules[r][1]:
                    to_remove.append(r)
            for r in to_remove:
                f.remove(r)
    # we still have multiple candidates for some fields -> reduce this
    while not all(len(f) == 1 for f in fields_candidate):
        for f in fields_candidate:
            if len(f) == 1:
                for k,c in enumerate(fields_candidate):
                    if c != f:
                        fields_candidate[k] = c.difference(f)
    # assert all(len(f) == 1 for f in fields_candidate)
    fields = [f.pop() for f in fields_candidate] # get rid of the sets
    # print(fields)
    count2 = 1
    for i,f in enumerate(fields):
        if f.startswith('departure'):
            count2 *= my_ticket[i]

    print("Step 1:", count1)
    print("Step 2:", count2)


