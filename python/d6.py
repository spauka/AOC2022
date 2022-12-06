def marker(line, count):
    for i in range(len(line)-count):
        if len(set(line[i:i+count])) == count:
            return i+count

with open("input6.txt") as f:
    line = f.readline().strip()
print(marker(line, 4))
print(marker(line, 14))