#!/usr/bin/env python

BLOCK = "#"
SPACE = " "

DEFAULT_DISP_MAP = {
    ' ' : SPACE,
    '.' : SPACE,
    '#' : BLOCK,
    0   : SPACE,
    1   : BLOCK,
}

class Grid:
    def __init__(self, default=0):
        self.grid = {}
        self.default = default
        self.x_min = 0
        self.y_min = 0
        self.x_max = 0
        self.y_max = 0

    def get(self, x, y):
        return self.grid.get((x, y), self.default)

    def width(self):
        return self.x_max - self.x_min + 1

    def height(self):
        return self.y_max - self.y_min + 1

    def set(self, x, y, value):
        self.x_min = min(self.x_min, x)
        self.y_min = min(self.y_min, y)
        self.x_max = max(self.x_max, x)
        self.y_max = max(self.y_max, y)
        self.grid[(x, y)] = value
    
    def set_origin(self, x, y):
        grid_old = self.grid.copy()
        self.grid = {}
        self.x_min, self.y_min, self.x_max, self.y_max = 0, 0, 0, 0
        for pos in grid_old:
            x_new, y_new = pos[0] - x, pos[1] - y
            self.set(x_new, y_new, grid_old[pos])

    def is_set(self, x, y):
        return (x, y) in self.grid
    
    def is_in(self, x, y):
        return (self.x_min <= x <= self.x_max \
                and self.y_min <= y <= self.y_max)
    
    def count(self, value):
        c = 0
        for k,v in self.grid.items():
            if v == value: c += 1
        return c

    def render(self, disp_map=DEFAULT_DISP_MAP):
        lines = []
        for y in range(self.y_min, self.y_max + 1):
            line = ""
            for x in range(self.x_min, self.x_max + 1):
                c = self.grid.get((x, y), self.default)
                if c in disp_map:
                    line += disp_map[c]
                else:
                    line += c
            lines.append(line)
        return '\n'.join(lines)


