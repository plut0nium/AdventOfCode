#!/usr/bin/python

from itertools import permutations
from copy import deepcopy

inputs = []
outputs = []
max_thruster = 0
sequence = None

def run(code):
    pos = 0
    while(True):
        instruction = code[pos] % 100
        if instruction in (1,2,5,6,7,8):
            if int((code[pos] / 100) % 10) == 1:
                addr_a = pos+1
            else:
                addr_a = code[pos+1]
            if int((code[pos] / 1000) % 10) == 1:
                addr_b = pos+2
            else:
                addr_b = code[pos+2]
            #print(pos, instruction, addr_a, addr_b)
            a = code[addr_a]
            b = code[addr_b]
            if instruction == 1:
                code[code[pos+3]] = a + b
                pos += 4
            elif instruction == 2:
                code[code[pos+3]] = a * b
                pos += 4
            elif instruction == 5:
                if a != 0:
                    pos = b
                else:
                    pos += 3
            elif instruction == 6:
                if a == 0:
                    pos = b
                else:
                    pos += 3
            elif instruction == 7:
                code[code[pos+3]] = 1 if a < b else 0
                pos += 4
            elif instruction == 8:
                code[code[pos+3]] = 1 if a == b else 0
                pos += 4
        elif instruction == 3:
            code[code[pos + 1]] = inputs.pop(0)
            pos += 2
        elif instruction == 4:
            if code[pos] >= 100: # only 1 argument
                c = code[pos+1]
            else:
                c = code[code[pos+1]]
            outputs.append(c)
            pos += 2
        elif instruction == 99:
            #print("Code halted :",code[pos],"@", pos)
            break
    return code

def run_loop(code, pos=0):
    while(True):
        instruction = code[pos] % 100
        if instruction in (1,2,5,6,7,8):
            if int((code[pos] / 100) % 10) == 1:
                addr_a = pos+1
            else:
                addr_a = code[pos+1]
            if int((code[pos] / 1000) % 10) == 1:
                addr_b = pos+2
            else:
                addr_b = code[pos+2]
            #print(pos, instruction, addr_a, addr_b)
            a = code[addr_a]
            b = code[addr_b]
            if instruction == 1:
                code[code[pos+3]] = a + b
                pos += 4
            elif instruction == 2:
                code[code[pos+3]] = a * b
                pos += 4
            elif instruction == 5:
                if a != 0:
                    pos = b
                else:
                    pos += 3
            elif instruction == 6:
                if a == 0:
                    pos = b
                else:
                    pos += 3
            elif instruction == 7:
                code[code[pos+3]] = 1 if a < b else 0
                pos += 4
            elif instruction == 8:
                code[code[pos+3]] = 1 if a == b else 0
                pos += 4
        elif instruction == 3:
            code[code[pos + 1]] = inputs.pop(0)
            pos += 2
        elif instruction == 4:
            if code[pos] >= 100: # only 1 argument
                c = code[pos+1]
            else:
                c = code[code[pos+1]]
            outputs.append(c)
            pos += 2
            break
        elif instruction == 99:
            #print("Code halted :",code[pos],"@", pos)
            return None, None
    return code, pos


if __name__ == "__main__":
    input_file = open("input", 'r')

    opcode_raw = input_file.read().strip()
    opcode = [int(x) for x in opcode_raw.split(",")]

    for p in permutations(range(5),5):
        for s in p:
            del inputs[:]
            amp_code = deepcopy(opcode)
            inputs.append(s)
            if len(outputs) != 0:
                inputs.append(outputs.pop(0))
            else:
                inputs.append(0)
            run(amp_code)
        if outputs[0] > max_thruster:
            sequence = p
            max_thruster = outputs[0]
        del outputs[:]
    
    print("Part 1:", max_thruster, "for sequence", sequence)

    for p in permutations(range(5,10),5):
        amp_code = [deepcopy(opcode) for i in range(len(p))]
        pos = [0 for i in range(len(p))]
        l = 0
        last_output = 0
        while(True):
            for i in range(len(p)):
                del inputs[:]
                if l == 0: # first loop use phase setting
                    inputs.append(p[i])
                if len(outputs) != 0:
                    inputs.append(outputs.pop(0))
                else:
                    inputs.append(0)
                amp_code[i], pos[i] = run_loop(amp_code[i], pos[i])
            last_output = outputs[0] if len(outputs) > 0 else last_output # needed because amps do not output in last loop
            if amp_code[-1] is None: # last amp has stopped
                break
            l += 1
        if last_output > max_thruster:
            sequence = p
            max_thruster = last_output

    print("Part 2:", max_thruster, "for sequence", sequence)
