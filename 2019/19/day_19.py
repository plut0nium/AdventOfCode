#!/usr/bin/env python
# -*- coding: utf-8 -*-

from intcode import IntCode
from grid import Grid

input_file = "input19.txt"

if __name__ == '__main__':
    with open(input_file, 'r') as f:
        code_raw = f.read().strip()
    code = [int(x) for x in code_raw.split(",")]

    beam = Grid()

    drone = IntCode(code)
    
    for x in range(50):
        for y in range(50):
            drone.reset()
            drone.run([x,y])
            beam.set(x,y,'#' if drone.output[0] == 1 else '.')
    
    print("Part 1:",beam.count("#"))

    # FUCKING 99 because of integer grid
    SHIP_WIDTH = 99
    SCAN_RADIUS = 5

    y = 1000
    # find beam width @ y = 1000
    for x in range(y):
        drone.reset()
        drone.run([x,y])
        if x == 0:
            in_beam_prev = False
        in_beam = True if drone.output[0] == 1 else False
        if in_beam and not in_beam_prev:
            x1 = x
        elif not in_beam and in_beam_prev:
            x2 = x-1
            break
        in_beam_prev = in_beam
    
    # calculate slopes
    m1 = y / x1
    m2 = y / x2
    spacing1 = SHIP_WIDTH * (1 + 1 / m1)
    y1 = int(m2 * spacing1 / (1 - m2 / m1))

    for y in range(y1-SCAN_RADIUS, y1+SCAN_RADIUS):
        y1 = y
        x2 = int(y1 / m2)
        # test x2
        in_beam_prev = True
        for x in range(x2-SCAN_RADIUS,x2+SCAN_RADIUS):
            drone.reset()
            drone.run([x,y])
            in_beam = True if drone.output[0] == 1 else False
            if not in_beam and in_beam_prev:
                x2 = x-1
                break
            in_beam_prev = in_beam
        # test x1
        y2 = y + SHIP_WIDTH
        x1 = int(y2 / m1)
        in_beam_prev = False
        for x in range(x1-SCAN_RADIUS,x1+SCAN_RADIUS):
            drone.reset()
            drone.run([x,y2])
            in_beam = True if drone.output[0] == 1 else False
            if in_beam and not in_beam_prev:
                x1 = x
                break
            in_beam_prev = in_beam
        #print(f"x1 {x1} - x2 {x2} - y1 {y1} - y2 {y2} - dx {x2 - x1}")
        if (x2 - x1) == SHIP_WIDTH:
            sol = x1 * 10000 + y1
            break
    
    print("Part 2:", sol)
    