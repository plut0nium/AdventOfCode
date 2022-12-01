#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict, deque

input_file = "input"
test_input = None
# test_input = [0,3,6]
# test_input = [1,3,2]
# test_input = [2,1,3]
# test_input = [1,2,3]
# test_input = [2,3,1]
# test_input = [3,2,1]
# test_input = [3,1,2]

def elves_game(starting, turns):
    spoken = defaultdict(list)
    # spoken = defaultdict(lambda : deque(maxlen=2)) # actually slower than lists...
    for i,s in enumerate(starting):
        spoken[s].append(i)
        ls = s
    for i in range(len(starting), turns):
        if len(spoken[ls]) <= 1:
            ls = 0
        else:
            ls = spoken[ls][-1] - spoken[ls][-2]
        spoken[ls].append(i)
    return ls


if __name__ == '__main__':
    if test_input is None:
        with open(input_file,'r') as f:
            starting = [int(i) for i in f.readline().strip().split(',')]
    else:
        starting = test_input
    
    # from datetime import datetime
    # startTime = datetime.now() # let's do some simple profiling...
    
    print("Step 1:", elves_game(starting, 2020))
    print("Step 2:", elves_game(starting, 30000000))

    # print(datetime.now() - startTime)
