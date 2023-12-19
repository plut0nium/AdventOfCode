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

OP = {">": gt, "<": lt}
rule_re = re.compile(r'(?:(\w+)([<>])(\d+):(\w+))|(\w+)')

def parse_part(p_str):
    return {k: int(v) for k, v in (a.split("=") for a in p_str[1:-1].split(","))}

def parse_workflow(w_str):
    name, rules_str = w_str.strip()[:-1].split("{")
    rules = []
    for r in rule_re.findall(rules_str):
        if not r[-1]:
            rules.append((r[3], r[0], OP[r[1]], int(r[2])))
        else:
            # default rule
            rules.append((r[-1], None, None, None))
    return name, rules

def inspect(part, workflows, workname=START):
    # return True if part is [A]ccepted according to workflows
    for r in workflows[workname]:
        if r[1] is None:
            dest = r[0]
            break
        op = r[2]
        if op(part[r[1]], r[3]):
            dest = r[0]
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
def part2(parts):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        workflows_str, parts_str = f.read().split("\n\n")
        workflows = {n:r for n, r in (parse_workflow(w.strip()) for w in workflows_str.split("\n"))}
        parts = [parse_part(p.strip()) for p in parts_str.split("\n") if len(p.strip())]
    print("Part #1 :", part1(parts, workflows))
    print("Part #2 :", part2(None))
