from utils import read_numbers

piles = [[] for _ in range(9)]
with open("input5.txt") as f:
    inp = f.readlines()
    instr = [read_numbers(x) for x in inp[10:]]

    for line in inp[:8]:
        for j, c in enumerate(line[1::4]):
            if c != " ":
                piles[j].append(c)
    for pile in piles:
        pile.reverse()
piles2 = [l[:] for l in piles]

for c, f, t in instr:
    for i in range(c):
        piles[t-1].append(piles[f-1].pop())

for c, f, t in instr:
    piles2[t-1].extend(piles2[f-1][-c:])
    piles2[f-1] = piles2[f-1][:-c]

print("".join(pile[-1] for pile in piles))
print("".join(pile[-1] for pile in piles2))
