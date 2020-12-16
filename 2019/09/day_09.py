#!/usr/bin/python

inputs = []
outputs = []

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
                print("Input buffer is empty : PAUSED @", pos)
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

if __name__ == "__main__":
    input_file = open("input", 'r')
    opcode_raw = input_file.read().strip()

    opcode = [int(x) for x in opcode_raw.split(",")]

    inputs.append(1)
    
    run(opcode)
    
    print("Part 1:", outputs)
    
    # reset opcode, inputs and outputs for part 2
    opcode = [int(x) for x in opcode_raw.split(",")]
    inputs.append(2)
    del outputs[:]
    
    run(opcode)
    
    print("Part 2:", outputs)