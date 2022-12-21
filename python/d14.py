from utils import InfiniteGrid, Coord, read_numbers
import numpy as np
from itertools import zip_longest

g = InfiniteGrid()

with open("input14.txt") as f:
    for line in (l.strip().split("->") for l in f):
        s1, s2 = read_numbers(line[0])
        for c1, c2 in (read_numbers(c) for c in line[1:]):
            # Fill in squares
            st1, en1 = min(s1, c1), max(s1, c1)
            st2, en2 = min(s2, c2), max(s2, c2)
            for r1, r2 in zip_longest(range(st1, en1+1), range(st2, en2+1), fillvalue=st1 if st1==en1 else st2):
                g[r1, -r2] = 1
            s1, s2 = c1, c2

def simulate_sand(with_floor=False):
    i = 0
    floor = g.bl[1] - 1
    while True:
        i += 1
        s = Coord(500, 0)
        while with_floor or s[1] > floor:
            if with_floor and s[1] == floor:
                g[s] = 2
                break
            elif g[s - (0, 1)] == 0:
                s = s - (0, 1)
            elif g[s - (1, 1)] == 0:
                s = s - (1, 1)
            elif g[s - (-1, 1)] == 0:
                s = s - (-1, 1)
            else:
                if s == Coord(500, 0):
                    return i
                g[s] = 2
                break
        else:
            return i-1

print((p1 := simulate_sand()))
print(simulate_sand(True) + p1)