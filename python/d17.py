import numpy as np
from utils import Coord, InfiniteGrid
from collections import deque
from itertools import cycle

rocks = [np.array([[1,1,1,1]]).T, 
         np.array([[0,1,0],[1,1,1],[0,1,0]]), 
         np.array([[1,0,0],[1,0,0],[1,1,1]]), 
         np.array([[1,1,1,1]]), 
         np.array([[1,1],[1,1]])]
rocks = cycle(np.nonzero(r == 1) for r in rocks)
movement = cycle(open("input17.txt").read().strip())
g = InfiniteGrid()
for x in range(7):
    g[x,0] = 1

def drop_rock(grid, next_rock, movement_iter, grid_width=7, start_x=2, start_height=4, count=1):
    # Figure out the starting position of the next rock
    offset = Coord(start_x, g.tl[1]+start_height)

    # Then drop the rock
    while True:
        # First the rock gets pushed by the wind
        new_offset = offset - (1, 0) if next(movement_iter) == "<" else offset + (1, 0)
        new_coords = [c + o for c, o in zip(next_rock, new_offset)]
        if np.any(new_coords[0] < 0) or np.any(new_coords[0] >= grid_width) or any(grid[x, y] != 0 for x, y in zip(*new_coords)): # Hit a wall
            new_offset = offset
        
        # Then the rock drops
        new_offset = new_offset - (0, 1)
        drop_coords = [c + o for c, o in zip(next_rock, new_offset)]
        if any(grid[x, y] for x, y in zip(*drop_coords)):
            new_coords = [c + o for c, o in zip(next_rock, new_offset + (0, 1))]
            for x, y in zip(*new_coords):
                grid[x, y] = count%9 + 1
            break
        offset = new_offset

def calc_height(start, diffs, i):
    i -= len(start)
    full_cycles, semi_cycles = divmod(i, len(diffs))
    return sum(start) + sum(diffs)*full_cycles + sum(diffs[:semi_cycles])

# Look for cycles
diffs = []
plen = 16
clen = -1
cycles = {}
dq = deque([0]*plen, maxlen=plen)
prev = 0
for i in range(2022):
    drop_rock(g, next(rocks), movement, count=i)
    diffs.append((diff := g.tr[1] - prev))
    dq.append(diff)
    prev = g.tr[1]
    if (ind := tuple(dq)) in cycles:
        clen = i - cycles[ind]
        print(f"Repeated cycle ({ind}) @ {i} with preiod: {clen}")
        offs = (i-plen)%clen
        start = diffs[:offs+1]
        diffs = diffs[-clen-plen:-plen]
        break
    cycles[ind] = i

print(calc_height(start, diffs, 2022))
print(calc_height(start, diffs, 1000000000000))