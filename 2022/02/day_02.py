#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

shifumi = {"A":"1", "B":"2", "C":"3",
           "X":"1", "Y":"2", "Z":"3" }
# Rock - Paper - Scissors
# R = 1, P = 2, S = 3
# -> X wins if X == Y+1 (mod 3) 

def part1(rounds):
    score = 0
    for r in rounds:
        if r[1] == r[0]:
            # draw
            score += r[1] + 3
        elif r[1]%3 == (r[0] + 1)%3:
            # win
            score += r[1] + 6
        else:
            # loose
            score += r[1]
    return score

def part2(rounds):
    score = 0
    for r in rounds:
        if r[1] == 1:
            # loose
            score += 3 if r[0] == 1 else (r[0] - 1)
        elif r[1] == 2:
            # draw
            score += r[0] + 3
        else:
            # win
            score += 1 if r[0] == 3 else (r[0] + 1)
            score += 6
    return score

if __name__ == '__main__':
    rounds = []
    for l in open(input_file).readlines():
        for k in shifumi.keys():
            l = l.replace(k, shifumi[k])
        r = [x for x in map(int,l.strip().split())]
        rounds.append(r)
    print("Part #1 :", part1(rounds))
    print("Part #2 :", part2(rounds))
