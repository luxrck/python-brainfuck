__version__ = "1.0.0"


def eval(source):
    code = Code(source)
    for _ in code.step():
        pass


class Code(object):
    def __init__(self, source):
        def parse(source):
            symtb = set([">", "<", "+", "-", ".", ",", "[", "]"])
            out = []
            last_bracket_indexs = []
            for line in source.split("\n"):
                for c in line:
                    if c == "#": break
                    elif c in symtb: out += [c]
                    if c == "[":
                        last_bracket_indexs += [len(out) - 1]
                    elif c == "]":
                        current_bracket_index = len(out) - 1
                        last_bracket_index = last_bracket_indexs.pop(-1)
                        out[last_bracket_index] = "[" + str(current_bracket_index)
                        out[current_bracket_index] = "]" + str(last_bracket_index)
            return out
        self.source = parse(source)
        self.cells = [0 for i in range(102400)]

        self.cp = 0
        self.ip = 0


    def step(self):
        while self.ip < len(self.source):
            yield (self.ip, self.source[self.ip], self.cp, self.cells[self.cp])
            i = self.source[self.ip]
            if i == ">":
                self.cp += 1
            elif i == "<":
                self.cp -= 1
            elif i == "+":
                self.cells[self.cp] += 1
            elif i == "-":
                self.cells[self.cp] -= 1
            elif i == ".":
                print("%c"%self.cells[self.cp], sep="", end="")
            elif i == ",":
                raw = input()
                if raw:
                    self.cells[self.cp] = raw.encode("utf-8")[0]
            elif i[0] == "[":
                if not self.cells[self.cp]:
                    self.ip = int(i[1:])
            elif i[0] == "]":
                if self.cells[self.cp]:
                    self.ip = int(i[1:])
            self.ip += 1
