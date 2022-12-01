#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test1.txt"

class SubMarine:
    def __init__(self):
        self.position = 0
        self.aim = 0
        self.depth = 0
    
    def move(self, c):
        if c[0] == "forward":
            self.position += c[1]
            self.depth += self.aim * c[1]
        elif c[0] == "down":
            self.aim += c[1]
        elif c[0] == "up":
            self.aim -= c[1]
        else:
            raise ValueError

if __name__ == '__main__':
    s = SubMarine()

    with open(input_file,'r') as f:
        commands = [(c, int(a)) for c, a in
                            [l.strip().split() for l in f.readlines()]]
    
    for c in commands:
        s.move(c)
    
    print(s.position * s.aim) # aim = depth in part 1
    print(s.position * s.depth)

