from functools import cmp_to_key

packets = []
with open("input13.txt") as f:
    for p1, p2, _ in zip(*[iter(f)]*3):
        packets.append((eval(p1), eval(p2)))

def cmp_packet(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return (p1 > p2) - (p1 < p2)
    elif isinstance(p1, list) and isinstance(p2, list):
        for pp1, pp2 in zip(p1, p2):
            if (c := cmp_packet(pp1, pp2)) != 0:
                return c
        return (len(p1) > len(p2)) - (len(p1) < len(p2))
    elif isinstance(p1, int):
        return cmp_packet([p1], p2)
    else:
        return cmp_packet(p1, [p2])

print(sum(i+1 for i, (pl, pr) in enumerate(packets) if cmp_packet(pl, pr) == -1))

packets = [x for y in packets for x in y]
packets.extend([[[2]], [[6]]])
packets.sort(key=cmp_to_key(cmp_packet))
print((packets.index([[2]])+1)*(packets.index([[6]])+1))
