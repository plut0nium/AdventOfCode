#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"
#input_file = "test02.txt"

C = [20+40*i for i in range(6)]

def process_cycle(cycle, X):
    if cycle in C:
        C.remove(cycle)
        return cycle*X
    return 0

def process_cycle_2(cycle, X):
    if (cycle-1)%40 in (X-1, X, X+1):
        return cycle-1
    return None

def display(p2):
    d = " "*240
    for p in p2:
        d = d[:p] + "#" + d[p+1:]
    return "\n".join([d[i*40:(i+1)*40] for i in range(6)])

if __name__ == '__main__':
    X = 1
    cycle = 0
    p1 = 0
    p2 = []
    for l in open(input_file, 'r').readlines():
        l = l.strip()
        if l.startswith('noop'):
            v = 0
        else:
            v = int(l.split()[1])
            cycle += 1
            p1 += process_cycle(cycle, X)
            tmp = process_cycle_2(cycle, X)
            if tmp is not None:
                p2.append(tmp)
        cycle += 1
        p1 += process_cycle(cycle, X)
        tmp = process_cycle_2(cycle, X)
        if tmp is not None:
            p2.append(tmp)
        X += int(v)

    print("Part #1 :", p1)
    print("Part #2 :", "\n", display(p2), sep="")
