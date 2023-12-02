#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

BAG_CONTENT = [12, 13, 14]

def parse_game(g):
    s = g.split(": ")
    id = int(s[0][5:])
    rounds = []
    for r in s[1].split("; "):
        counts = [0,0,0]
        for t in r.split(', '):
            n, c = t.split(" ")
            if c == "red":
                counts[0] += int(n)
            elif c == "green":
                counts[1] += int(n)
            elif c == "blue":
                counts[2] += int(n)
            else:
                print("ERROR")
        rounds.append(counts)
    return id, rounds

def part1(games, content):
    p1 = 0
    for g in games:
        impossible = False
        for r in g[1]:
            if any(r[i] > content[i] for i in range(3)):
                impossible = True
                break
        if impossible:
            #print("Impossible : ", g[0])
            continue
        p1 += g[0]
    return p1
        
def part2(games):
    p2 = 0
    for g in games:
        m = [max(v) for v in zip(*g[1])]
        p2 += reduce(lambda x, y: x*y, m)
    return p2
        
if __name__ == '__main__':
    games = []
    for l in open(input_file, 'r').readlines():
        games.append(parse_game(l.strip()))
    print("Part #1 :", part1(games, BAG_CONTENT))
    print("Part #2 :", part2(games))
