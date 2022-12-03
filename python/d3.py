from functools import reduce
m = lambda x: ord(x)-ord('a')+1 if x.islower() else ord(x)-ord('A')+27

sacks = []
with open("input3.txt") as f:
    for line in f:
        line = [m(x) for x in line.strip()]
        sacks.append((set(line[:len(line)//2]), set(line[len(line)//2:])))

print(sum((s1&s2).pop() for s1, s2 in sacks))

s = 0
for p in zip(*[iter(sacks)]*3):
    s += reduce(set.intersection, (reduce(set.union, x) for x in p)).pop()
print(s)