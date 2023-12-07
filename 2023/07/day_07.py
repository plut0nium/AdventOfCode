#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import Counter
from functools import cmp_to_key

CARD_LABELS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def parse_hands(hands_list):
    hands = []
    for g in hands_list:
        h, b = g.strip().split()
        b = int(b)
        hands.append((h,b))
    return hands

def compare_hands(h1, h2):
    # return  1 if h1 > h2
    #        -1 if h1 < h2
    #         0 if equal
    h1 = h1[0]
    h2 = h2[0]
    c1 = Counter(h1)
    c2 = Counter(h2)
    # print(c1)
    # print(c2)
    if max(c1.values()) > max(c2.values()):
        return 1
    elif max(c1.values()) < max(c2.values()):
        return -1
    else:
        if max(c1.values()) == 2:
            # check for two pairs
            cc1 = Counter(c1.values())
            cc2 = Counter(c2.values())
            # print(cc1)
            # print(cc2)
            if cc1[2] == 2 and cc2[2] < 2:
                return 1
            elif cc2[2] == 2 and cc1[2] < 2:
                return -1
            else:
                pass
        if max(c1.values()) == 3:
            # check for Full House
            if 2 in c1.values() and 2 not in c2.values():
                return 1
            elif 2 in c2.values() and 2 not in c1.values():
                return -1
            else:
                pass
        # equality
        for i in range(5):
            if CARD_LABELS.index(h1[i]) < CARD_LABELS.index(h2[i]):
                return 1
            elif CARD_LABELS.index(h1[i]) > CARD_LABELS.index(h2[i]):
                return -1
            else:
                pass
    return 0

def part1(hands):
    hands.sort(key=cmp_to_key(compare_hands))
    return sum([(i+1) * h[1] for i,h in enumerate(hands)])

def part2(hands):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        hands = parse_hands(f.readlines())
    print("Part #1 :", part1(hands))
    print("Part #2 :", part2(hands))
