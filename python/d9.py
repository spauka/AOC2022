from utils import Coord, Neighbours

def step(head, tail):
    dist = head - tail
    if dist.mag_l2() < 2:
        return head, tail, 0
    dir = min((dist.dist(dir), dir) for dir in Neighbours.DIRS.values())[1]
    return head, tail+dir, 1

def sim(instrs, rlen):
    rope = [Coord(0, 0)]*rlen
    visited = set((Coord(0, 0),))
    for d, s in instrs:
        for _ in range(s):
            rope[0] = rope[0] + Neighbours.DIRS[d]
            for j in range(rlen-1):
                rope[j], rope[j+1], c = step(rope[j], rope[j+1])
                if not c:
                    break
            visited.add(rope[-1])
    return len(visited)

instrs = []
with open("input9.txt") as f:
    for d, s in (l.strip().split() for l in f):
        instrs.append((d, int(s)))

print(sim(instrs, 2))
print(sim(instrs, 10))
