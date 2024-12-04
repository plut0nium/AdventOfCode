#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

WORD = "XMAS"
DIRS = [(-1,-1), ( 0,-1), ( 1,-1),
        (-1, 0),          ( 1, 0),
        (-1, 1), ( 0, 1), ( 1, 1)]

def part1(word_search):
    found = 0
    for y, r in enumerate(word_search):
        for x, c in enumerate(r):
            if c != WORD[0]:
                continue
            # c = "X"
            for d in DIRS:
                x_new, y_new = x, y
                for i in range(1,4):
                    x_new = x_new + d[0]
                    y_new = y_new + d[1]
                    if x_new < 0 or x_new >= len(r) or \
                       y_new < 0 or y_new >= len(word_search):
                        # no need to continue in this direction
                        break
                    if word_search[y_new][x_new] != WORD[i]:
                        break
                    if i == 3:
                        found += 1                        
    return found


def part2(word_search):
    return None


if __name__ == '__main__':
    word_search = []
    for l in open(input_file, 'r').readlines():
        word_search.append(l.strip())
    print(part1(word_search))
    print(part2(word_search))
