#!/usr/bin/env python

BLOCK = "#"
SPACE = " "

DEFAULT_DISP_MAP = {
    ' ' : SPACE,
    0   : SPACE,
    '.' : SPACE,
    '#' : BLOCK,
    1   : BLOCK,
    '^' : '^'
}

class Grid:
    def __init__(self, default=0):
        self.grid = {}
        self.default = default
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        self.frame = 0
        self.frames = []
        self.fonts = None

    def get(self, x, y):
        return self.grid.get((x, y), self.default)

    def width(self):
        return self.max_x - self.min_x + 1

    def height(self):
        return self.max_y - self.min_y + 1

    def set(self, x, y, value):
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)
        self.grid[(x, y)] = value

    def value_set(self, x, y):
        return (x, y) in self.grid

    def enum_grid(self, callback, include_missing=True):
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if include_missing:
                    callback(x, y, self.grid.get((x, y), self.default))
                else:
                    if (x, y) in self.grid:
                        callback(x, y, self.grid[(x, y)])

    def show_grid(self, log, disp_map=DEFAULT_DISP_MAP):
        for y in range(self.min_y, self.max_y + 1):
            line = ""
            for x in range(self.min_x, self.max_x + 1):
                c = self.grid.get((x, y), self.default)
                if c in disp_map:
                    line += disp_map[c]
                else:
                    line += c
            print(line)

