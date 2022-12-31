from itertools import product
from collections import deque
from utils import Coord, read_numbers

with open("input18.txt") as f:
    cubes = {Coord(read_numbers(l)) for l in f}
bbox = tuple((min(c[i] for c in cubes), max(c[i] for c in cubes)) for i in range(3))

def neighbours(coord):
    for c, o in product(range(3), [-1, 1]):
        offset = Coord(o if i==c else 0 for i in range(3))
        yield offset + coord

outside = set()
inside = set()
def bfs(coord):
    tovisit = deque([coord])
    visited = set()
    while tovisit:
        ccoord = tovisit.pop()
        for next_coord in neighbours(ccoord):
            if any(c not in range(*bc) for c, bc in zip(next_coord, bbox)):
                return True, visited # OUTSIDE
            if next_coord in visited or next_coord in cubes:
                continue
            visited.add(next_coord)
            tovisit.appendleft(next_coord)
    return False, visited # INSIDE
        
faces = 0
outside_faces = 0
for cube in cubes:
    for next_coord in neighbours(cube):
        if next_coord not in cubes:
            if next_coord in outside:
                outside_faces += 1
            elif next_coord not in inside:
                isoutside, visited = bfs(next_coord)
                if isoutside:
                    outside |= visited
                    outside_faces += 1
                else:
                    inside |= visited
            faces += 1
print(faces)
print(outside_faces)
