# -*- coding: utf-8 -*-

data = [int(x) for x in open('input.txt').readline().split(" ")]
#data = [int(x) for x in open('input_test.txt').readline().split(" ")]

def parse(data):
    children, metas = data[:2]
    data = data[2:]
    totals = 0

    for i in range(children):
        total, data = parse(data)
        totals += total

    totals += sum(data[:metas])

    return (totals, data[metas:])
    

total, remaining = parse(data)

print('part 1:', total)
