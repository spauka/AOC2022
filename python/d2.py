inputs = []
mapping = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

with open("input2.txt") as f:
    for line in f:
        inputs.append([mapping[x] for x in line.strip().split()])

score = 0
for inp in inputs:
    p1, p2 = inp
    res = (1 + p2 - p1)%3
    score += p2 + 3*res
print(score)

score = 0
for inp in inputs:
    p1, p2 = inp
    if p2 == 1:
        res = (p1 - 1)%3 + 3
        score += res if res else 3
    elif p2 == 2:
        score += p1 + 3
    elif p2 == 3:
        score += (p1%3) + 1 + 6
print(score)