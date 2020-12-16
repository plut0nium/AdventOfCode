#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

DECK_SIZE = 10007
input_file = "input22.txt"

#DECK_SIZE = 10
#input_file = "input_test4.txt"

def make_deck(size):
    return [x for x in range(size)]

def deal_into_new(stack):
    d = stack.copy()
    d.reverse()
    return d

def cut(n, stack):
    #n = n % len(stack) # not necessary if abs(n) < len(stack)
    d = stack.copy()
    return d[n:] + d[:n]

def deal_with_increment(n, stack):
    l = len(stack)
    #n = n % len(stack) # not necessary if abs(n) < len(stack)
    d = [0 for _ in range(l)]
    for i in range(l):
        d[i*n % l] = stack[i]
    return d

if __name__ == '__main__':
    deck = make_deck(DECK_SIZE)
    with open(input_file, 'r') as f:
        for line in f.readlines():
            if "new" in line:
                #print("Deal into new")
                deck = deal_into_new(deck)
            elif "cut" in line:
                c = int(re.findall(r'[-+]?\d+', line)[0])
                #print("Cut", c)
                deck = cut(c, deck)
            elif "increment" in line:
                i = int(re.findall(r'[-+]?\d+', line)[0])
                #print("Deal with increment", i)
                deck = deal_with_increment(i, deck)
            else:
                #unknown
                print("Error: unknow:", line)
                break
    #print(deck)
    print("Part 1:", deck.index(2019))

