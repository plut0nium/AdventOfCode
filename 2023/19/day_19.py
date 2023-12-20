#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

START = "in"
ACCEPT = "A"
REJECT = "R"

from operator import lt, gt
import re
from copy import copy
from functools import reduce

OP = {">": gt, "<": lt}
rule_re = re.compile(r'(?:(\w+)([<>])(\d+):(\w+))|(\w+)')

def parse_part(p_str):
    return {k: int(v) for k, v in (a.split("=") for a in p_str[1:-1].split(","))}

def parse_workflow(w_str):
    name, rules_str = w_str.strip()[:-1].split("{")
    rules = []
    for r in rule_re.findall(rules_str):
        if not r[-1]:
            rules.append((r[0], OP[r[1]], int(r[2]), r[3]))
        else:
            # default rule
            rules.append((r[-1], ))
    return name, rules

def inspect(part, workflows, workname=START):
    # return True if part is [A]ccepted according to workflows
    for r in workflows[workname]:
        if len(r) == 1:
            # default rule
            dest = r[0]
            break
        op = r[1] # comparison operator
        if op(part[r[0]], r[2]):
            dest = r[-1]
            break
    if dest == ACCEPT:
        return True
    elif dest != REJECT:
        return inspect(part, workflows, dest)
    return False

@timing
def part1(parts, workflows):
    assert(START in workflows)
    return sum(sum(p.values()) for p in parts if inspect(p, workflows))

@timing
def part2(workflows):
    assert(START in workflows)
    accepted = 0
    stack = [(START, {n:range(1,4001) for n in "xmas"})]

    def _check_rule(rule, ratings):
        nonlocal accepted, stack
        if r[-1] == ACCEPT:
            # all remaining parts are [A]ccepted
            accepted += reduce(lambda a,b: a*b, [len(v) for v in ratings.values()])
        elif r[-1] == REJECT:
            pass # do nothing with [R]ejected
        else:
            # remaining parts to be checked against next rule
            stack.append((r[-1], ratings))

    while len(stack):
        rule, ratings = stack.pop()
        for r in workflows[rule]:
            if len(r) == 1:
                # default rule
                _check_rule(r, ratings)
                break
            else:
                assert(r[2] in ratings[r[0]])
                ratings_split = copy(ratings)
                if r[1] == lt: # LT
                    ratings_split[r[0]] = range(ratings[r[0]].start, r[2])
                    ratings[r[0]] = range(r[2], ratings[r[0]].stop)
                else: # GT
                    ratings_split[r[0]] = range(r[2]+1, ratings[r[0]].stop)
                    ratings[r[0]] = range(ratings[r[0]].start, r[2]+1)
                _check_rule(r, ratings_split)
    return accepted


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        workflows_str, parts_str = f.read().split("\n\n")
        workflows = {n:r for n, r in (parse_workflow(w.strip()) for w in workflows_str.split("\n"))}
        parts = [parse_part(p.strip()) for p in parts_str.split("\n") if len(p.strip())]
    print("Part #1 :", part1(parts, workflows))
    print("Part #2 :", part2(workflows))
