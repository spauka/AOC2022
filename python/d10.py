from enum import Enum, auto

class Instr:
    INSTRS = {}
    TIME = 1
    def __init__(self):
        self.args = []

    def __init_subclass__(cls):
        Instr.INSTRS[cls.__name__.lower()] = cls

    @classmethod
    def to_instr(self, name, *args):
        return Instr.INSTRS[name](*(int(x) for x in args))

    def exec(self, regs):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} {' '.join(str(x) for x in self.args)}"

class Noop(Instr):
    pass

class AddX(Instr):
    TIME = 2
    def __init__(self, val):
        super().__init__()
        self.args.append(val)

    def exec(self, regs):
        regs.X += self.args[0]

class State(Enum):
    LOAD = auto()
    EXEC = auto()
    FIN = auto()

class Registers:
    __slots__ = ("X",)
    def __init__(self):
        self.X = 1

class CPU:
    def __init__(self):
        self.curr_instr = None
        self.remain = 0
        self.reset()

    def reset(self):
        self.tick = 0
        self.regs = Registers()
        self.state = State.LOAD

    def run(self, instrs, callback=None):
        self.state = State.LOAD
        instrs = iter(instrs)
        while self.state is not State.FIN:
            if self.state is State.LOAD:
                try:
                    self.curr_instr = next(instrs)
                    self.remain = self.curr_instr.TIME
                    self.state = State.EXEC
                except StopIteration:
                    self.state = State.FIN
            elif self.state is State.EXEC:
                self.remain -= 1
                self.tick += 1
                if callback is not None:
                    callback(self)
                if self.remain == 0:
                    self.curr_instr.exec(self.regs)
                    self.curr_instr = None
                    self.state = State.LOAD

cpu = CPU()
instrs = []
with open("input10.txt") as f:
    for line in (l.strip().split() for l in f):
        instrs.append(Instr.to_instr(*line))

def check_times(cpu):
    if (cpu.tick - 20)%40 == 0:
        check_times.sum += cpu.tick * cpu.regs.X
check_times.sum = 0

cpu.run(instrs, check_times)
print(check_times.sum)

def draw_sprites(cpu):
    dist = abs(cpu.tick % 40 - 1 - cpu.regs.X)
    print ("#" if dist <= 1 else ".", end="")
    if cpu.tick%40 == 0:
        print()

cpu.reset()
cpu.run(instrs, draw_sprites)
