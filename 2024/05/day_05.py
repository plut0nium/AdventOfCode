#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"


def check_update(update, rules):
    for i, p in enumerate(update[:-1]):
        if p in rules and all(r in rules[p] for r in update[i+1:]):
            continue
        else:
            return False
    return True


def part1(updates, rules):
    correct = [u for u in updates if check_update(u, rules)]
    return sum(c[len(c)//2] for c in correct)


def part2(updates, rules):
    incorrect = [u for u in updates if not check_update(u, rules)]
    for u in incorrect:
        while not check_update(u, rules):
            for i, p in enumerate(u):
                if p not in rules:
                    # no rule for page -> move to end
                    u.append(u.pop(i))
                    continue
                for j, q in enumerate(u[i+1:]):
                    if q in rules[p]:
                        # OK -> q to be printed after p
                        continue
                    else:
                        # NOK -> swap
                        u[i] = q
                        u[i+1+j] = p
                        break
    return sum(c[len(c)//2] for c in incorrect)


if __name__ == '__main__':
    rules = {}
    updates = []
    with open(input_file, 'r') as f:
        rules_str, updates_str = f.read().split("\n\n")
    for s in rules_str.strip().splitlines():
        a, b = map(int, s.split("|"))
        if a not in rules:
            rules[a] = [b]
        else:
            rules[a].append(b)
    for s in updates_str.strip().splitlines():
        updates.append(list(map(int, s.split(","))))
    print(part1(updates, rules))
    print(part2(updates, rules))
