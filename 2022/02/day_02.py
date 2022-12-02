#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

shifumi = {"A":"0", "B":"1", "C":"2",
           "X":"0", "Y":"1", "Z":"2" }
# Rock - Paper - Scissors
# R = 0, P = 1, S = 2
# -> X wins if X == Y+1 (mod 3) 

def part1(rounds):
    score = 0
    for r in rounds:
        result = (r[1] - r[0] + 1) % 3 # 0 = lose, 1 = draw, 2 = win
        score += (r[1] + 1) + result * 3
    return score

def part2(rounds):
    score = 0
    for r in rounds:
        # r[1] is the result here
        my_choice = (r[0] + (r[1] - 1)) % 3
        score += (my_choice + 1) + r[1] * 3
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
