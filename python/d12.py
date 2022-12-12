from utils import Grid, Coord
from collections import deque
import numpy as np

g = Grid.load_dense_file("input12.txt", conv_char=True)
start = Coord(np.transpose(np.nonzero(g.grid == ord('S')))[0])
end = Coord(np.transpose(np.nonzero(g.grid == ord('E')))[0])
g.grid -= ord('a') - 1
g[start] = 1
g[end] = 26

def bfs(grid, end):
    dists = np.zeros_like(g.grid) - 1
    dists[end] = 0
    nodes = deque([end])
    while nodes:
        curr = nodes.popleft()
        curr_height = grid[curr]
        for next_coord in grid.n[curr].coords:
            if curr_height - grid[next_coord] <= 1 and dists[next_coord] == -1:
                dists[next_coord] = dists[curr] + 1
                nodes.append(next_coord)
    return dists

dists = bfs(g, end)
print(dists[start])

starts = [Coord(c) for c in np.transpose(np.nonzero(g.grid == 1))]
dists = sorted(dists[c] for c in starts if dists[c] >= 0)
print(dists[0])
