#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

def parse_card(card_str):
    card_id, card_numbers = card_str.split(":")
    card_id = int(card_id[4:])
    winning, numbers = map(lambda s: [int(i) for i in s.strip().split()],
                           card_numbers.split("|"))
    return card_id, winning, numbers

def count_card_wins(card):
    card_id, winning, numbers = card
    return len([n for n in numbers if n in winning])

def part1(cards):
    total_points = 0
    for c in cards:
        card_points = count_card_wins(c)
        total_points += 2 ** (card_points - 1) if card_points > 0 else 0
    return total_points
    
def part2(cards):
    card_count = [1 for _ in cards]
    for c in cards:
        card_wins = count_card_wins(c)
        if card_wins > 0:
            for i in range(card_wins):
                card_count[c[0] + i] += card_count[c[0] -1]
    return sum(card_count)


if __name__ == '__main__':
    cards = []
    for l in open(input_file, 'r').readlines():
        cards.append(parse_card(l.strip()))
    print("Part #1 :", part1(cards))
    print("Part #2 :", part2(cards))
