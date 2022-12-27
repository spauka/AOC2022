from itertools import product
from utils import Coord, read_numbers

with open("input18.txt") as f:
    cubes = {Coord(read_numbers(l)) for l in f}

faces = 0
for cube in cubes:
    for c, o in product(range(3), [-1, 1]):
        offset = Coord(o if i==c else 0 for i in range(3))
        if cube+offset not in cubes:
            faces += 1
print(faces)
