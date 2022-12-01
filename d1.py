weights = []

with open("input1.txt") as f:
    s = 0
    for line in f:
        if not (line := line.strip()):
            weights.append(s)
            s = 0
            continue
        s += int(line)

weights.sort()
print(weights[-1])
print(sum(weights[-3:]))
