#!/usr/bin/python

target = 19690720

def run(code):
    pos = 0
    while(True):
        if code[pos] not in (1,2):
            #print("Code halted :",code[pos],"@", pos)
            break
        a = code[code[pos+1]]
        b = code[code[pos+2]]
        if code[pos] == 1:
            c = a + b
        else: # 2
            c = a * b
        code[code[pos+3]] = c
        pos += 4
    return code


if __name__ == "__main__":
    input_file = open("input", 'r')

    opcode_raw = input_file.read().strip()
    opcode = [int(x) for x in opcode_raw.split(",")]

    opcode[1] = 12
    opcode[2] = 2

    print("Part 1:", run(opcode)[0])

    for n,v in ((n, v) for n in range(100) for v in range(100)):
        #reset opcode
        opcode = [int(x) for x in opcode_raw.split(",")]
        opcode[1] = n
        opcode[2] = v
        if run(opcode)[0] == target:
            print("noun: {}, verb: {}".format(n,v))
            print("Part 2:", 100*n+v)
            break


            


