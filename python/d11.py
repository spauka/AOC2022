from collections import deque
from functools import reduce
from operator import mul
from utils import read_numbers

class Monkey:
    MONKEYS = []
    STRESS = lambda x: x // 3
    def __init__(self, objects, operation, test):
        # Keep track of monkeys
        self.id = len(Monkey.MONKEYS)
        Monkey.MONKEYS.append(self)

        self.objects = deque(objects)
        self.oobjects = self.objects.copy()
        self.operation = operation
        self.test = test
        self.activity = 0

    def reset(self):
        self.activity = 0
        self.objects = self.oobjects.copy()

    def take_turn(self):
        while len(self.objects) > 0:
            self.activity += 1
            object = Monkey.STRESS(self.operation(self.objects.popleft()))
            action = self.test(object)
            Monkey.MONKEYS[action].objects.append(object)

divisors = []
with open("input11.txt") as f:
    for m in zip(*[iter(l.strip() for l in f)]*7):
        objects = read_numbers(m[1])
        div = read_numbers(m[3])[0]
        divisors.append(div)
        m_true = read_numbers(m[-3])[0]
        m_false = read_numbers(m[-2])[0]
        op_str = m[2].split("=")[1].strip()
        test = lambda x, m_true=m_true, m_false=m_false, div=div: m_true if x%div == 0 else m_false
        operation = lambda x, op_str=op_str: eval(op_str, {"old": x})

        new_monkey = Monkey(objects, operation, test)

for i in range(20):
    for m in Monkey.MONKEYS:
        m.take_turn()
print(reduce(mul, sorted(m.activity for m in Monkey.MONKEYS)[-2:]))

for m in Monkey.MONKEYS:
    m.reset()
pdiv = reduce(mul, divisors)
Monkey.STRESS = lambda x, pdiv=pdiv: x % pdiv

for i in range(10000):
    for m in Monkey.MONKEYS:
        m.take_turn()
print(reduce(mul, sorted(m.activity for m in Monkey.MONKEYS)[-2:]))
