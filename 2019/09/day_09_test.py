#!/usr/bin/python

from intcode import IntCode

if __name__ == "__main__":
    input_file = open("input", 'r')
    code_raw = input_file.read().strip()

    code = [int(x) for x in code_raw.split(",")]

    intcode = IntCode(code)
    intcode.run(1)
    
    
    print("Part 1:", intcode.output)

    intcode.reset()
    intcode.run(2)
    
    print("Part 2:", intcode.output)