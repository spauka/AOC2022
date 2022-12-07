import re
import functools

class TreeNode:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirs = {}
        self.files = {}

    def __str__(self):
        return "/" if self.parent is None else f"{str(self.parent)}{self.name}/"

    @functools.cached_property
    def size(self):
        return sum(self.files.values()) + sum(n.size for n in self.subdirs.values())

    def __iter__(self):
        yield self
        for node in self.subdirs.values():
            for val in node:
                yield val

root = TreeNode("", None)

with open("input7.txt") as f:
    for line in (l.strip() for l in f):
        if (m := re.findall("\\$ cd ([a-zA-Z/.]+)", line)):
            if m[0] == "/":
                cd = root
            elif m[0] == "..":
                cd = cd.parent
            else:
                if m[0] not in cd.subdirs:
                    cd.subdirs[m[0]] = TreeNode(m[0], cd)
                cd = cd.subdirs[m[0]]
        elif (m := re.findall("dir ([a-zA-Z]+)", line)):
            if m[0] not in cd.subdirs:
                cd.subdirs[m[0]] = TreeNode(m[0], cd)
        elif (m := re.findall("([0-9]+) ([a-zA-Z.]+)", line)):
            cd.files[m[0][1]] = int(m[0][0])

free_space = 70000000 - root.size
print(sum(dir.size for dir in root if dir.size <= 100000))
print(sorted(n.size for n in root if (n.size + free_space) > 30000000)[0])
