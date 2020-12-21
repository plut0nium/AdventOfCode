#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
import functools

input_file = "input"
# input_file = "test1.txt"

if __name__ == '__main__':
    count1, count2 = 0, 0

    food = []
    all_ingredients = set()
    all_allergens = set()

    with open(input_file,'r') as f:
        for l in f.readlines():
            if not l.strip():
                continue
            ingredients, allergens = l.strip()[:-1].split("(contains")
            ingredients = {i.strip() for i in ingredients.split(" ") if i.strip()}
            allergens = {a.strip() for a in allergens.split(",")}
            all_ingredients |= ingredients
            all_allergens |= allergens
            food.append((ingredients, allergens))
    
    maybe_in = {}
    for a in all_allergens:
        candidate = set()
        for f_i, f_a in food:
            if a in f_a:
                 candidate = candidate & f_i if candidate else f_i
        maybe_in[a] = candidate

    safe = deepcopy(all_ingredients)
    # for i in maybe_in.values():
    #     safe -= i
    safe = functools.reduce(lambda x,y: x - y, [safe] + [i for i in maybe_in.values()])

    for i, _ in food:
        count1 += len(safe & i)
    
    cdil = deepcopy(maybe_in)
    for _ in all_allergens:
        for a in all_allergens:
            if len(cdil[a]) == 1:
                for a2 in all_allergens:
                    if a2 != a:
                        cdil[a2] -= cdil[a]

    print("Step 1:", count1)
    print("Step 2:", ','.join(cdil[a].pop() for a in sorted(all_allergens)))

