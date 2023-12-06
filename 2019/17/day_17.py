#!/usr/bin/env python
# -*- coding: utf-8 -*-

from intcode import IntCode
from grid import Grid

input_file = "input17.txt"

if __name__ == '__main__':
    with open(input_file, 'r') as f:
        code_raw = f.read().strip()
    code = [int(x) for x in code_raw.split(",")]

    dir_map = {'^':0, '>':1, 'v':2, '<':3}
    dir_coord = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}

    intcode = IntCode(code)
    intcode.run()
    
    scaff = Grid()
    x,y = 0,0
    for s in intcode.output:
        if s == 10: # \n
            x = 0
            y += 1
            continue
        scaff.set(x,y,chr(s))
        if chr(s) in dir_map:
            curr_dir = dir_map[chr(s)]
            curr_coord = (x,y)
        x += 1
    #scaff.show_grid(None)
    
    alignment = 0
    for x in range(scaff.width()):
        for y in range(scaff.height()):
            if scaff.get(x,y) != "#":
                continue
            if scaff.get(x-1,y) == "#" \
                and scaff.get(x+1,y) == "#" \
                and scaff.get(x,y-1) == "#" \
                and scaff.get(x,y+1) == "#":
                alignment += x*y
    print("Part 1:", alignment)
    
    import numpy as np
    
    path = []
    forw_count = 0
    while True:
        x_fw, y_fw = tuple(np.add(curr_coord, dir_coord[curr_dir]))
        
        if scaff.get(x_fw, y_fw) != '#':
            if forw_count > 0: 
                path.append(forw_count)
                forw_count = 0
            left_dir, right_dir = (curr_dir - 1) % 4, (curr_dir + 1) % 4
            x_left, y_left = tuple(np.add(curr_coord, dir_coord[left_dir]))
            x_right, y_right = tuple(np.add(curr_coord, dir_coord[right_dir]))
            if scaff.get(x_left, y_left) == '#':
                path.append('L')
                curr_dir = left_dir
            elif scaff.get(x_right, y_right) == '#':
                path.append('R')
                curr_dir = right_dir
            else:
                break
        else:
            forw_count += 1
            curr_coord = (x_fw, y_fw)

    #print("Path:", ','.join(map(str, path)))

    seq_A = "L,12,R,4,R,4"
    seq_B = "R,12,R,4,L,12"
    seq_C = "R,12,R,4,L,6,L,8,L,8"
    main = "A,B,B,C,C,A,A,B,B,C"
    
    vac_sequence = [ord(c) for c in main]
    vac_sequence.append(ord('\n'))
    vac_sequence.extend([ord(c) for c in seq_A])
    vac_sequence.append(ord('\n'))
    vac_sequence.extend([ord(c) for c in seq_B])
    vac_sequence.append(ord('\n'))
    vac_sequence.extend([ord(c) for c in seq_C])
    vac_sequence.append(ord('\n'))
    vac_sequence.append(ord('n'))
    vac_sequence.append(ord('\n'))
    
    intcode.reset()
    intcode.mem[0] = 2
    intcode.add_input(vac_sequence)
    
    intcode.run()

    print("Part 2:", intcode.output[-1])
    