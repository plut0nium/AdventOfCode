#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time

input_file = "input"
# input_file = "test01.txt"

decryption_key = 811589153

def mix(file, n=1):
    l = len(file)
    fileindex = [i for i in range(l)]
    for _ in range(n):
        for i, v in enumerate(file):
            if v == 0:
                continue
            j = fileindex.index(i)
            x = fileindex.pop(j)        
            k = (j + v) % (l - 1)
            fileindex.insert(k, x)
    return [file[i] for i in fileindex]

def grove_coordinates(file):
    l = len(file)
    return sum(file[i] for i in 
               ((file.index(0)+m) % l for m in [1000, 2000, 3000]))

if __name__ == '__main__':
    start_time = time()
    with open(input_file, 'r') as f:
        file = list(map(int, (n.strip() for n in f.readlines())))

    print("Part #1 :", grove_coordinates(mix(file)))

    file2 = [f * decryption_key for f in file]
    
    print("Part #2 :", grove_coordinates(mix(file2, 10)))
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
