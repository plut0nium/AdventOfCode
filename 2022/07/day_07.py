#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

FS_SIZE = 70000000
SPACE_REQUIRED = 30000000

def dir_size(d, fs):
    s = 0
    for f in fs[d]:
        if isinstance(f, str):
            # child dir
            c = d + "/" + f if len(d) > 1 else d + f
            s += dir_size(c, fs)
        else:
            s += f
    return s

if __name__ == '__main__':
    fs = dict()
    current_path = []
    for c in open(input_file).readlines():
        c = c.strip()
        if c[:4] == '$ cd':
            if c[5:] == '..':
                current_path.pop()
            elif c[5:] == '/':
                current_path = ['/']
            else:
                current_path.append(c[5:])
        elif c[:4] == '$ ls':
            pass
        else:
            p = current_path[0] + "/".join(current_path[1:])
            if p not in fs:
                fs[p] = []
            t, n = c.split()
            if t == 'dir':
                # add subdir
                fs[p].append(n)
            else:
                # just store file size
                fs[p].append(int(t))

    s = []
    for k in fs.keys():
        s.append(dir_size(k, fs))
    unused_space = FS_SIZE - max(s)
    candidate = FS_SIZE
    for t in sorted(s):
        if t >= (SPACE_REQUIRED - unused_space) and t < candidate:
            candidate = t
            break # because we sorted s

    print("Part #1 :", sum((t for t in s if t <= 100000)))
    print("Part #2 :", candidate)
