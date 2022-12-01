#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_data = '137826495'
input_data = '389125467' # test
moves = 3

if __name__ == '__main__':
    count1, count2 = 0, 0

    cups = [int(c) for c in input_data]
    current_cup = 0
    
    for _ in range(moves):
        pick_up = cups[current_cup+1:current_cup+4]
        
        destination = cups[current_cup] - 1
        if destination < min(cups): destination = max(cups)
        while destination in pick_up:
            destination -= 1
            if destination < min(cups): destination = max(cups)
    
        for _ in range(3):
            cups.pop(current_cup + 1)
        cups = cups[:cups.index(destination)+1] + pick_up + cups[cups.index(destination)+1:]
        
        current_cup += 1

    print("Step 1:", count1)
    print("Step 2:", count2)

