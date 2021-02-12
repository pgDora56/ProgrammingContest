h, w = map(int, input().split())
mod = 10**9+7


class Cell:
    def __init__(self):
        self.way = 0
        self.diag = 0
        self.hori = 0
        self.vert = 0

    def get_way_from(self, direction):
        if self.way == 0:
            return 0
        if direction == "diag":
            return (self.way + self.diag) % mod
        if direction == "hori":
            return (self.way + self.hori) % mod
        if direction == "vert":
            return (self.way + self.vert) % mod
        raise AttributeError("Invalid direction")


heavy = [[Cell() for _ in range(w)] for _ in range(h)]
heavy[0][0].way = 1
prev = []
current = []
for i in range(h):
    s = input()
    if i == 0:
        line0 = heavy[0]
        for j in range(1, w):
            if s[j] == "#":
                continue
            else:
                way = line0[j-1].get_way_from("hori")
                line0[j].hori = way
                line0[j].way = (line0[j].way + way) % mod
        prev = line0
    else:
        current = heavy[i]
        for j in range(w):
            if s[j] == "#":
                continue
            if j == 0:
                way = prev[0].get_way_from("vert")
                current[0].vert = way
                current[0].way = (current[0].way + way) % mod
            else:
                vway = prev[j].get_way_from("vert")
                hway = current[j-1].get_way_from("hori")
                dway = prev[j-1].get_way_from("diag")
                current[j].vert = vway
                current[j].hori = hway
                current[j].diag = dway
                current[j].way = (current[j].way + vway + hway + dway) % mod
        prev = current

print(prev[w-1].way)
