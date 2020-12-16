#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

inputs = []
outputs = []

hull = {}

arity = {99:0, 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1}

def run(code, pos=0, rel_base=0):
    while(True):
        instruction = code[pos] % 100
        #print(instruction, "@", pos)
        # parameters
        arg_addr = []
        for a in range(arity[instruction]):
            mode = int((code[pos] / 10 ** (2+a)) % 10)
            if mode == 1: # immediate mode
                aa = pos+(a+1)
            elif mode == 2: # relative mode
                aa = rel_base + code[pos+(a+1)]
            else: # position mode
                aa = code[pos+(a+1)]
            arg_addr.append(aa)
        # extend memory if required
        if len(arg_addr) > 0 and max(arg_addr) > len(code) - 1:
            code.extend([0]*(max(arg_addr)-len(code)+1))
        #instructions
        if instruction == 1:
            code[arg_addr[2]] = code[arg_addr[0]] + code[arg_addr[1]]
            pos += 4
        elif instruction == 2:
            code[arg_addr[2]] = code[arg_addr[0]] * code[arg_addr[1]]
            pos += 4
        elif instruction == 3:
            if len(inputs) == 0:
                #print("Input buffer is empty : PAUSED @", pos)
                break
            code[arg_addr[0]] = inputs.pop(0)
            pos += 2
        elif instruction == 4:
            outputs.append(code[arg_addr[0]])
            pos += 2
        elif instruction == 5:
            if code[arg_addr[0]] != 0:
                pos = code[arg_addr[1]]
            else:
                pos += 3
        elif instruction == 6:
            if code[arg_addr[0]] == 0:
                pos = code[arg_addr[1]]
            else:
                pos += 3
        elif instruction == 7:
            code[arg_addr[2]] = 1 if code[arg_addr[0]] < code[arg_addr[1]] else 0
            pos += 4
        elif instruction == 8:
            code[arg_addr[2]] = 1 if code[arg_addr[0]] == code[arg_addr[1]] else 0
            pos += 4
        elif instruction == 9:
            rel_base += code[arg_addr[0]]
            pos += 2
        elif instruction == 99:
            print("Code halted :",code[pos],"@", pos)
            return None, None, None
    return code, pos, rel_base


def paint(opcode, start):
    robot_pos = (0,0)
    robot_dir = 0 # 0: UP, 1 = LEFT, 2 = DOWN, 3 = RIGHT
    inputs.append(start) # start the robot on an area of given color
    o, p, r = opcode, 0, 0
    while(True):
        o,p,r = run(o,p,r)
        if o is None:
            print("Robot halted")
            break
        if len(outputs) == 2:
            c, d = outputs[0:2]
            del outputs[0:2]
            if len(outputs) != 0:
                print("DEBUG - Outputs should be 0")
        else:
            print("No output produced - STOP @",p)
            break
        # paint the area
        hull[robot_pos] = c
        # turn the robot
        if d == 0:
            robot_dir += 1
        elif d == 1:
            robot_dir -= 1
        robot_dir %= 4
        # move the robot
        x,y = robot_pos
        if robot_dir == 0:
            y += 1
        elif robot_dir == 1:
            x -= 1
        elif robot_dir == 2:
            y -= 1
        elif robot_dir == 3:
            x += 1
        robot_pos = (x,y)
        if robot_pos in hull:
            inputs.append(hull[robot_pos])
        else:
            inputs.append(0)


if __name__ == '__main__':
    input_file = open("input", 'r')
    opcode_raw = input_file.read().strip()

    opcode = [int(x) for x in opcode_raw.split(",")]

    paint(opcode, 0)
    
    print("Part 1:", len(hull))

    hull = {}
    inputs = []
    outputs = []
    
    min_x, min_y, max_x, max_y = 0,0,0,0
    
    opcode = [int(x) for x in opcode_raw.split(",")]
    
    paint(opcode, 1)
    
    for x,y in hull.keys():
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    
    registration_id = Image.new('1', (max_x-min_x+1,max_y-min_y+1))
    for p, v in hull.items():
        if v == 1:
            x = p[0] - min_x
            y = max_y - p[1]
            registration_id.putpixel((x,y),1)
    part2_output = "part2.png"
    registration_id.save(part2_output)
    
    print("Part 2: see", part2_output)
        