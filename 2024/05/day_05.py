#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"


def part1(updates, rules):
    correct = []
    for u in updates:
        is_correct = True
        for i, p in enumerate(u[:-1]):
            if p in rules and all(r in rules[p] for r in u[i+1:]):
                continue
            else:
                is_correct = False
                break
        if is_correct:
            correct.append(u)
    return sum(c[len(c)//2] for c in correct)


def part2(updates, rules):

    return None


if __name__ == '__main__':
    rules = {}
    updates = []
    with open(input_file, 'r') as f:
        rules_str, updates_str = f.read().split("\n\n")
    for s in rules_str.strip().split("\n"):
        a, b = map(int, s.split("|"))
        if a not in rules:
            rules[a] = [b]
        else:
            rules[a].append(b)
    for s in updates_str.strip().split("\n"):
        updates.append(list(map(int, s.split(","))))
    print(part1(updates, rules))
    print(part2(updates, rules))
