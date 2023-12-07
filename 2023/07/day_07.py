#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import Counter
from functools import cmp_to_key, partial

CARD_LABELS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARD_LABELS2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def parse_hands(hands_list):
    hands = []
    for g in hands_list:
        h, b = g.strip().split()
        b = int(b)
        hands.append((h,b))
    return hands

def compare_hands(h1, h2, use_joker=False):
    # return  1 if h1 > h2
    #        -1 if h1 < h2
    #         0 if equal
    h1 = h1[0]
    h2 = h2[0]
    c1 = Counter(h1)
    c2 = Counter(h2)
    if use_joker:
        # part 2
        for c in [c1, c2]:
            # add the joker count to the most common (non-joker) card
            if c['J'] == 0 or c['J'] == 5:
                # no joker, or 5 jokers
                # do nothing
                continue
            if c.most_common(1)[0][0] == 'J':
                # joker is the most common
                c[c.most_common(2)[1][0]] += c['J']
            else:
                c[c.most_common(1)[0][0]] += c['J']
            del c['J']
    if max(c1.values()) > max(c2.values()):
        return 1
    elif max(c1.values()) < max(c2.values()):
        return -1
    else:
        if max(c1.values()) == 2:
            # check for two pairs
            cc1 = Counter(c1.values()) # counter of counter, probably overkill
            cc2 = Counter(c2.values())
            if cc1[2] == 2 and cc2[2] < 2:
                # h1 has 2 pairs
                return 1
            elif cc2[2] == 2 and cc1[2] < 2:
                # h2 has 2 pairs
                return -1
            else:
                # both have 2 pairs
                pass
        if max(c1.values()) == 3:
            # check for Full House
            if 2 in c1.values() and 2 not in c2.values():
                return 1
            elif 2 in c2.values() and 2 not in c1.values():
                return -1
            else:
                pass
        # tie
        if use_joker:
            # part 2
            _card_labels = CARD_LABELS2
        else:
            _card_labels = CARD_LABELS
        for i in range(5):
            if _card_labels.index(h1[i]) < _card_labels.index(h2[i]):
                return 1
            elif _card_labels.index(h1[i]) > _card_labels.index(h2[i]):
                return -1
            else:
                pass
    return 0

def part1(hands):
    hands.sort(key=cmp_to_key(compare_hands))
    return sum([(i+1) * h[1] for i,h in enumerate(hands)])

def part2(hands):
    hands.sort(key=cmp_to_key(partial(compare_hands, use_joker=True)))
    return sum([(i+1) * h[1] for i,h in enumerate(hands)])


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        hands = parse_hands(f.readlines())
    print("Part #1 :", part1(hands))
    print("Part #2 :", part2(hands))
