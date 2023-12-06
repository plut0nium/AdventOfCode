#!/usr/bin/python

inputs = [5]
outputs = []

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


if __name__ == "__main__":
    input_file = open("input", 'r')

    opcode_raw = input_file.read().strip()
    opcode = [int(x) for x in opcode_raw.split(",")]

    #for i in range(3):
    #    opcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    #    run(opcode)

    run(opcode)
    
    print("Part 2:", outputs)




            


