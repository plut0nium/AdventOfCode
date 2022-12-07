#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
input_file = "test01.txt"

def dir_size(d, fs):
    s = 0
    for f in fs[d]:
        if isinstance(f, str):
            s += dir_size(f, fs)
        else:
            s += f
    return s

if __name__ == '__main__':
    fs = dict()
    current_dir = None
    for c in open(input_file).readlines():
        c = c.strip()
        if c[:4] == '$ cd':
            current_dir = c[5:]
        elif c[:4] == '$ ls':
            pass
        else:
            if current_dir not in fs:
                fs[current_dir] = []
            t, n = c.split()
            if t == 'dir':
                fs[current_dir].append(n)
            else:
                fs[current_dir].append(int(t))

    t = 0
    for k in fs.keys():
        s = dir_size(k, fs)
        if s <= 100000:
            t += s

    print("Part #1 :", t)
    # print("Part #2 :", None)
