#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

PKT_LEN = 4
MSG_LEN = 14

def find_marker(msg, l):
    for i in range(l-1,len(msg)):
        if len(set(msg[i-(l-1):i+1])) == l:
            return i
    return None

if __name__ == '__main__':
    for m in open(input_file).readlines():
        m = m.strip()
        print("Part #1 :", find_marker(m, PKT_LEN)+1)
        print("Part #2 :", find_marker(m, MSG_LEN)+1)
