#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import Counter
from functools import cmp_to_key, partial

CARD_LABELS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def parse_hands(hands_list):
    hands = []
    for g in hands_list:
        h, b = g.strip().split()
        b = int(b)
        hands.append((h,b))
    return hands

def get_card_rank(card, use_joker=False):
    if use_joker and card == 'J':
        return 0
    return len(CARD_LABELS) - CARD_LABELS.index(card)

def compare_hands(h1, h2, use_joker=False):
    # return  1 if h1 > h2
    #        -1 if h1 < h2
    #         0 if equal
    c1 = Counter(h1[0])
    c2 = Counter(h2[0])
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
            c12 = list(c1.values()).count(2)
            c22 = list(c2.values()).count(2)
            if c12 == 2 and c22 < 2:
                # h1 has 2 pairs
                return 1
            elif c22 == 2 and c12 < 2:
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
        for i in range(5):
            if get_card_rank(h1[0][i], use_joker) > get_card_rank(h2[0][i], use_joker):
                return 1
            elif get_card_rank(h1[0][i], use_joker) < get_card_rank(h2[0][i], use_joker):
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
