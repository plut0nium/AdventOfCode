#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import Counter
CARD_LABELS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def parse_hands(hands_list):
    hands = []
    for g in hands_list:
        h, b = g.strip().split()
        b = int(b)
        hands.append((h,b))
    return hands

def compare_hands(h1, h2):
    # return True if h1 > h2
    c1 = Counter(h1)
    c2 = Counter(h2)
    # print(c1)
    # print(c2)
    if max(c1.values()) > max(c2.values()):
        return True
    elif max(c1.values()) < max(c2.values()):
        return False
    else:
        if max(c1.values()) == 2:
            # check for two pairs
            cc1 = Counter(c1.values())
            cc2 = Counter(c2.values())
            # print(cc1)
            # print(cc2)
            if cc1[2] == 2 and cc2[2] < 2:
                return True
            elif cc2[2] == 2 and cc1[2] < 2:
                return False
            else:
                pass
        if max(c1.values()) == 3:
            # check for Full House
            if 2 in c1.values() and 2 not in c2.values():
                return True
            elif 2 in c2.values() and 2 not in c1.values():
                return False
            else:
                pass
        # equality
        for i in range(5):
            if CARD_LABELS.index(h1[i]) < CARD_LABELS.index(h2[i]):
                return True
            elif CARD_LABELS.index(h1[i]) > CARD_LABELS.index(h2[i]):
                return False
            else:
                pass
    return None

def part1(hands):
    for i in range(len(hands)-1, 0, -1):
        for j in range(i-1):
            if compare_hands(hands[j][0], hands[j+1][0]):
                # permute
                hands[j], hands[j+1] = hands[j+1], hands[j]
    print(hands)
    return sum([(i+1) * h[1] for i,h in enumerate(hands)])

def part2(hands):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        hands = parse_hands(f.readlines())
    print("Part #1 :", part1(hands))
    print("Part #2 :", part2(hands))
