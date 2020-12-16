#!/usr/bin/python
# -*- coding: utf-8 -*-

from grid import Grid
from intcode import IntCode

def calc(program):
    grid = Grid()
    grid.set(0, 0, ".")

    x, y = 0, 0
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    next_x, next_y = 0, 0
    final_x, final_y = 0, 0
    
    # Build the entire map
    first = True
    while True:
        if first:
            # The first step doesn't have output yet
            first = False
        else:
            state = program.output.pop(0)
            if state == 0:
                # Hit a wall, mark it
                grid.set(next_x, next_y, "#")
            elif state == 1 or state == 2:
                x, y = next_x, next_y
                # We moved, mark the cell
                grid.set(x, y, ".")
                # And, if we found the oxygen sensor, note that
                # we keep going to build up the entire map
                if state == 2:
                    final_x, final_y = x, y

        # First off, try moving to an unknown cell
        found_dir = False
        for i in range(len(dirs)):
            next_x = x + dirs[i][0]
            next_y = y + dirs[i][1]
            if (next_x, next_y) not in grid.grid:
                program.add_input(i + 1)
                found_dir = True
                break

        if not found_dir:
            # Nope, nothing interesting to do, mark
            # this cell as "dead" ('x' means not a wall, but
            # already visited)
            grid.set(x, y, "x")
            for i in range(len(dirs)):
                next_x = x + dirs[i][0]
                next_y = y + dirs[i][1]
                # And look for another cell to walk to
                # Any non-visited cell will do
                if grid.get(next_x, next_y) == ".":
                    program.add_input(i + 1)
                    found_dir = True
                    break

        if not found_dir:
            # We're stuck, this means we finished
            # Do two flood fills
            todo = [(0, 0, 0)]
            done = set()
            done.add((0, 0))

            last_step = 0
            while len(todo) > 0:
                tx, ty, s = todo.pop(0)
                if s > last_step:
                    grid.save_frame()
                    last_step = s
                # Just change the color for the animation
                grid.set(tx, ty, "RobotStep")
                for xo, yo in dirs:
                    ttx, tty = tx + xo, ty + yo
                    if grid.get(ttx, tty) != "#":
                        if (ttx, tty) not in done:
                            if (ttx, tty) == (final_x, final_y):
                                # We found the oxygen sensor, add one
                                # to the steps, and report it
                                print("Steps to sensor: " + str(s + 1))
                                todo = []
                            else:
                                done.add((ttx, tty))
                                todo.append((ttx, tty, s+1))

            # And now take a pass at finding the distance from the
            # sensor to all of the cells
            todo = [(final_x, final_y, 0)]
            done = set()
            done.add((final_x, final_y))
            last_step = 0
            while len(todo) > 0:
                tx, ty, s = todo.pop(0)
                if s > last_step:
                    grid.save_frame()
                    last_step = s
                grid.set(tx, ty, "Oxygen")
                for xo, yo in dirs:
                    ttx, tty = tx + xo, ty + yo
                    if grid.get(ttx, tty) != "#":
                        if (ttx, tty) not in done:
                            done.add((ttx, tty))
                            todo.append((ttx, tty, s+1))
                if len(todo) == 0:
                    print("Steps to flood oxygen: " + str(s))

            # grid.draw_frames(color_map={
            #     0: (0, 0, 0),
            #     'x': (0, 0, 0),
            #     '#': (255, 255, 255),
            #     'RobotStep': (255, 255, 0),
            #     'Oxygen': (32, 32, 255),
            # })

            #Grid.make_animation()
            # All done
            return

        program.run()
        
    return 0

            


if __name__ == '__main__':

    input_file = open("input15.txt", 'r')
    code_raw = input_file.read().strip()

    code = [int(x) for x in code_raw.split(",")]

    intcode = IntCode(code)
    calc(intcode)
   
    
    print("Part 1:", None)
