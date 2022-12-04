from utils import read_numbers

pairs = []
with open("input4.txt") as f:
    for line in f:
        p11, p12, p21, p22 = read_numbers(line)
        pairs.append((set(range(p11, p12+1)), set(range(p21, p22+1))))

count1, count2 = 0, 0
for p1, p2 in pairs:
    if (p1.issubset(p2)) or (p2.issubset(p1)):
        count1 += 1
    if (p1 & p2):
        count2 += 1
print(count1)
print(count2)