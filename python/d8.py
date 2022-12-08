from utils import Grid
from itertools import chain
import numpy as np

g = Grid.load_dense_file("input8.txt")
visible = set()

def cv(l, m=-1):
    for i, v in enumerate(l):
        if v > m:
            m = v
            yield i

for x in range(g.shape[0]):
    for y in cv(g[x, :]):
        visible.add((x, y))
    for y in cv(g[x, ::-1]):
        visible.add((x, g.shape[1]-y-1))

for y in range(g.shape[1]):
    for x in cv(g[:, y]):
        visible.add((x, y))
    for x in cv(g[::-1, y]):
        visible.add((g.shape[0]-x-1, y))

views = []
for x, y in g.iter_coord():
    left = np.where(g[:x, y][::-1] >= g[x, y])[0]
    left = left[0] if left.size else x

    right = np.where(g[x+1:, y] >= g[x, y])[0]
    right = right[0] if right.size else g.shape[0]-x-1

    up = np.where(g[x, :y][::-1] >= g[x, y])[0]
    up = up[0] if up.size else y

    down = np.where(g[x, y+1:] >= g[x, y])[0]
    down = down[0] if down.size else g.shape[1]-y-1

    views.append(left*right*up*down)

print(len(visible))
print(sorted(views)[-1])
