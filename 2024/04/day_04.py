#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

WORD = "XMAS"
DIRS = [(-1,-1), ( 0,-1), ( 1,-1),
        (-1, 0),          ( 1, 0),
        (-1, 1), ( 0, 1), ( 1, 1)]
DIRS_DIAG = [DIRS[0], DIRS[2], DIRS[7], DIRS[5]]


def part1(word_search):
    found = 0
    for y, r in enumerate(word_search):
        for x, c in enumerate(r):
            if c != WORD[0]:
                continue
            # c = "X"
            for d in DIRS:
                x_new, y_new = x, y
                for i in range(1,len(WORD)):
                    x_new = x_new + d[0]
                    y_new = y_new + d[1]
                    if x_new < 0 or x_new >= len(r) or \
                       y_new < 0 or y_new >= len(word_search):
                        # out of grid
                        # -> no need to continue in this direction
                        break
                    if word_search[y_new][x_new] != WORD[i]:
                        # not the expected letter
                        break
                    if i == (len(WORD) - 1):
                        # reached the end of the word
                        found += 1                        
    return found


def part2(word_search):
    found = 0
    w = word_search
    for y, r in enumerate(w):
        if y == 0 or y == (len(w) - 1):
            # skip first and last rows
            continue
        for x, c in enumerate(r):
            if x == 0 or x == (len(r) - 1):
                # skip first and last cols
                continue
            if c != "A":
                continue
            diags = ((w[y-1][x-1]+w[y+1][x+1]),
                     (w[y-1][x+1]+w[y+1][x-1]))
            if all(d in ("MS","SM") for d in diags):
                # both diagonals are MAS|SAM
                found += 1
    return found


if __name__ == '__main__':
    word_search = []
    for l in open(input_file, 'r').readlines():
        word_search.append(l.strip())
    print(part1(word_search))
    print(part2(word_search))
