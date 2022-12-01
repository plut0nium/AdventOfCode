#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test1.txt"

OPEN = ['(','[','{','<']
CLOSE = [')',']','}','>']
SCORE = [3, 57, 1197, 25137]

if __name__ == '__main__':
    
    with open(input_file,'r') as f:
        chunks = [l.strip() for l in f.readlines()]

    s1 = 0
    s2 = []
    for k in chunks:
        o = []
        corrupted = False
        for c in k:
            if c in OPEN:
                o.append(c)
            elif c in CLOSE:
                if OPEN.index(o[-1]) == CLOSE.index(c):
                    _ = o.pop()
                else:
                    #print(k, " -> ", c)
                    s1 += SCORE[CLOSE.index(c)]
                    corrupted = True
                    break
            else:
                raise ValueError("Unknown character", c)
        if not corrupted:
            s = 0
            r = [CLOSE[OPEN.index(c)] for c in reversed(o)]
            for c in r:
                s = (s * 5) + (CLOSE.index(c) + 1)
            s2.append(s)
            
    print(s1)
    print(sorted(s2)[int(len(s2)/2)])