#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test1.txt"

boards = []
scores = []

with open(input_file,'r') as f:
    draw = [int(i) for i in f.readline().strip().split(",")]
    _ = f.readline()
    b = []
    while True:
        l = f.readline()
        if not l: # empty line = EOF
            if len(b):
                boards.append(b)
            break
        if l.strip():
            b.append([int(i) for i in l.strip().split()])
        else: # empty line -> new board
            boards.append(b)
            b = []

def is_winner(b):
    for l in b:
        if l.count('X') == len(l):
            return True
    for i in range(len(b[0])):
        column = [l[i] for l in b]
        if column.count('X') == len(column):
            return True
    return False

def calc_score(b):
    return sum(n for l in b for n in l if n != 'X')

for d in draw:
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == d:
                    boards[i][j][k] = 'X'
    for b in boards:
        if is_winner(b):
            scores.append(d * calc_score(b))
            boards.remove(b)

print(scores[0])
print(scores[-1])


