#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test1.txt"
#input_file = "test2.txt"

class Display:
    DECODE = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9
    }
    
    def __init__(self, s):
        p, d = l.split(" | ")
        self.patterns = [set(a) for a in p.split()]
        self.value = [set(a) for a in d.split()]
        self.mapping = {}
    
    def make_mapping(self):
        freq = {}
        for s in 'abcdefg':
            freq[s] = len([a for a in self.patterns if s in a])
        for s,f in freq.items():
            if f == 4:
                self.mapping[s] = 'e'
            elif f == 6:
                self.mapping[s] = 'b'
            elif f == 9:
                self.mapping[s] = 'f'
            elif f == 8: # a or c
                for p in self.patterns:
                    if len(p) == 2: # digit 1
                        if s in p:
                            self.mapping[s] = 'c'
                        else:
                            self.mapping[s] = 'a'
            elif f == 7: # d or g
                for p in self.patterns:
                    if len(p) == 4: # digit 4
                        if s in p:
                            self.mapping[s] = 'd'
                        else:
                            self.mapping[s] = 'g'
            else:
                raise ValueError("Incorrect frequency", f)
    
    def read(self):
        if len(self.mapping) == 0:
            self.make_mapping()
        a = []
        for digit in self.value:
            v = ''.join(sorted(self.mapping[c] for c in digit))
            a.append(self.DECODE[v])
        return int(''.join(map(str, a)))

if __name__ == '__main__':
    displays = []
    
    with open(input_file,'r') as f:
        for l in f.readlines():
            displays.append(Display(l))
    
    print(len([v for d in displays for v in d.value if len(v) in (2,3,4,7)]))
    
    print(sum(d.read() for d in displays))
    