#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import mul
from functools import reduce

input_file = "input"
input_file = "test1.txt"

OPS = [ sum,
        lambda x:reduce(mul, x),
        min,
        max,
        None,
        lambda x:int(x[0] > x[1]),
        lambda x:int(x[0] < x[1]),
        lambda x:int(x[0] == x[1])
    ]

class PacketStream():
    def __init__(self, data):
        self.data = bin(int('1'+data.strip(),16))[3:]
        self.pos = 0
        self.versions = 0

    def read(self, n):
        self.pos += n
        return int(self.data[self.pos-n:self.pos], 2)

    def readpacket(self):
        self.versions += self.read(3)
        tid = self.read(3)
        if tid == 4:
            # litteral
            v = 0
            while True:
                flag = self.read(1)
                v = (v << 4) + self.read(4)
                if flag == 0:
                    return v
        else:
            # operator
            if self.read(1) == 0:
                # read n bits
                vals = []
                n = self.read(15)
                limit = self.pos + n
                while self.pos < limit:
                    vals.append(self.readpacket())
            else:
                # read n subpackets
                vals = [self.readpacket() for i in range(self.read(11))]
            return OPS[tid](vals)

if __name__ == '__main__':
    for l in open(input_file).readlines():
        stream = PacketStream(l.strip())
        result = stream.readpacket()
        print('part 1:', stream.versions, 'part 2:', result)

