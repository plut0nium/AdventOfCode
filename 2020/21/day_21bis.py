# -*- coding: utf-8 -*-

import functools, collections
from itertools import product

ale, all_ingr = {}, collections.Counter()


for line in open("test1.txt").read().splitlines():
    ingrs, algens = line.split(" (contains ")
    ingrs, algens = set(ingrs.split()), set(algens[:-1].split(", "))
    
    for ingr in ingrs: 
        all_ingr[ingr] += 1
    for algen in algens: 
        ale[algen] = ale[algen] & ingrs if algen in ale else ingrs.copy()
    

safe_map = functools.reduce(lambda x,y:x-y, [set(all_ingr)] + [ale[algen]for algen in ale])

print("Part 1:",sum(all_ingr[ingr] for ingr in safe_map))

for _,a1 in product(ale,ale): 
    ale = {a2: ale[a2] - ale[a1] if len(ale[a1]) == 1 and a1! = a2 else ale[a2] for a2 in ale}

print("Part 2:",','.join(map(lambda x: ale[x].pop(), sorted(ale))))

