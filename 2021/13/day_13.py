#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
#input_file = "test1.txt"

display = defaultdict(lambda: " ")

def fold(paper, f):
    p = set()
    for dot in paper:
        if f[0] == 'x':
            if dot[0] > f[1]:
                p.add((f[1]-(dot[0]-f[1]),dot[1]))
            else:
                p.add(dot)
        elif f[0] == 'y':
            if dot[1] > f[1]:
                p.add((dot[0],f[1]-(dot[1]-f[1])))
            else:
                p.add(dot)
        else:
            raise ValueError("Unknown axis", f[0])
    return p

paper = [set()]
folds = []

if __name__ == '__main__':
    with open(input_file,'r') as f:
        for l in f.readlines():
            if l.startswith("fold"):
                a,b = l.strip().split("=")
                folds.append((a[-1],int(b)))
            elif len(l.strip()):
                x,y = map(int, l.strip().split(","))
                paper[0].add((x,y))
            else:
                pass # empty line

    x_min, y_min = 0, 0
    for f in folds:
        paper.append(fold(paper[-1], f))
        if f[0] == 'x':
            x_min = f[1]
        else:
            y_min = f[1]

    print(len(paper[1]))
    for d in paper[-1]:
        display[d] = '#'
    for y in range(y_min):
        print("".join(display[(x,y)] for x in range(x_min)))
            


