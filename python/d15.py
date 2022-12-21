from typing import List
from utils import Range, read_numbers, Coord
import numpy as np
import tqdm

sensors: List[Coord] = []
beacons: List[Coord] = []

with open("input15.txt") as f:
    for sx, sy, bx, by in (read_numbers(l, allow_negative=True) for l in f):
        sensors.append(Coord(sx, sy))
        beacons.append(Coord(bx, by))

def valid_ranges(y, sensors, beacons):
    ranges = []
    # Find positions at y that can't contain a beacon
    for s, b in zip(sensors, beacons):
        d, dy = s.dist(b), abs(s[1] - y)
        if d >= dy:
            r = Range(s[0] - (d-dy), s[0] + (d-dy))
            i = 0
            while i < len(ranges):
                if ranges[i].contains(r):
                    break
                elif r.contains(ranges[i]):
                    ranges.pop(i)
                    continue
                elif r.overlaps(ranges[i]):
                    nr = r + ranges[i]
                    ranges.pop(i)
                    r = nr
                    continue
                i += 1
            else:
                ranges.append(r)
    return ranges

#print(sum(len(r) for r in valid_ranges(10, sensors, beacons)) - len(set(b for b in beacons if b[1] == 10)))
print(sum(len(r) for r in valid_ranges(2_000_000, sensors, beacons)) - len(set(b for b in beacons if b[1] == 2_000_000)))
xrange = Range(0, 4_000_000)
for y in tqdm.tqdm(range(4_000_000 + 1)):
    ranges = valid_ranges(y, sensors, beacons)
    if len(ranges) > 1:
        x = ranges[0].stop + 1
        break
print(x*4_000_000 + y)
