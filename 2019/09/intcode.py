#!/usr/bin/env python
# -*- coding: utf-8 -*-

arity = {99:0, 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1}

class IntCode:
    def __init__(self, code):
        if not all(type(i) is int for i in code):
            raise RuntimeError('IntCode error')
        self.mem = code
        self.mem_orig = self.mem.copy() # keep a copy of the original IntCode
        self.iptr = 0
        self.base = 0
        self.input = []
        self.output = []
        self.halted = False
    
    def _index(self, n):
        # assert(n > 0 and n <= arity[self._get_instruction()])
        mode = self.mem[self.iptr] // 10**(n + 1) % 10
        try:
            if mode == 0: # position mode
                return self.mem[self.iptr + n]
            elif mode == 1: # direct mode
                return self.iptr + n
            elif mode == 2: # relative mode
                return self.base + self.mem[self.iptr + n]
            else:
                raise RuntimeError(f'Bad mode: {mode}')
        except IndexError as _:
            # uninitialized memory read as 0
            return 0

    def _get_instruction(self):
        return self.mem[self.iptr] % 100

    def _get_arg(self, n):
        try:
            return self.mem[self._index(n)]
        except IndexError as _:
            # uninitialized memory read as 0
            return 0
    
    def _set_arg(self, n, val):
        i = self._index(n)
        if i < len(self.mem):
            self.mem[i] = val
        else:
            # extend memory
            self.mem.extend(0 for _ in range(len(self.mem), i+1))
            self.mem[-1] = val
    
    def add_input(self, inp):
        if type(inp) is int:
            self.input.append(inp)
        elif len(inp) >= 1 and all(type(i) is int for i in inp):
            self.input.extend(inp)
        elif len(inp) == 0:
            pass
        else:
            raise RuntimeError(f'Bad input: {inp}')
    
    def run(self, input=None):
        if input is not None:
            self.add_input(input)
        while True:
            instruction = self._get_instruction()
            #instructions
            if instruction == 1:
                self._set_arg(3, self._get_arg(1) + self._get_arg(2))
                self.iptr += arity[instruction] + 1
            elif instruction == 2:
                self._set_arg(3, self._get_arg(1) * self._get_arg(2))
                self.iptr += arity[instruction] + 1
            elif instruction == 3:
                if len(self.input) == 0:
                    #print("Input buffer is empty : PAUSED @", pos)
                    break
                self._set_arg(1, self.input.pop(0))
                self.iptr += arity[instruction] + 1
            elif instruction == 4:
                self.output.append(self._get_arg(1))
                self.iptr += arity[instruction] + 1
            elif instruction == 5:
                self.iptr = self._get_arg(2) if self._get_arg(1) != 0 \
                                else self.iptr + arity[instruction] + 1
            elif instruction == 6:
                self.iptr = self._get_arg(2) if self._get_arg(1) == 0 \
                                else self.iptr + arity[instruction] + 1
            elif instruction == 7:
                self._set_arg(3, int(self._get_arg(1) < self._get_arg(2)))
                self.iptr += arity[instruction] + 1
            elif instruction == 8:
                self._set_arg(3, int(self._get_arg(1) == self._get_arg(2)))
                self.iptr += arity[instruction] + 1
            elif instruction == 9:
                self.base += self._get_arg(1)
                self.iptr += arity[instruction] + 1
            elif instruction == 99:
                self.halted = True
                #print("Code halted :",code[pos],"@", pos)
                break
            else:
                raise RuntimeError(f'bad opcode {mem[ip]}')
        return 0

    def reset(self):
        self.mem = self.mem_orig.copy()
        self.input.clear()
        self.output.clear()
        self.iptr = 0
        self.base = 0
        self.halted = False

if __name__ == '__main__':
    intcode = IntCode([99])

