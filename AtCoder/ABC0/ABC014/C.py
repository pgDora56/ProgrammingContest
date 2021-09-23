class Color:
    def __init__(self):
        self.inc = 0
        self.dec = 0

    def increase(self):
        self.inc += 1

    def decrease(self):
        self.dec += 1

    def buy(self, prev):
        return prev + self.inc - self.dec


n = int(input())
colors = [Color() for _ in range(1000001)]

for _ in range(n):
    a, b = map(int,input().split())
    colors[a].increase()
    if b != 1000000:
        colors[b+1].decrease()

prev = 0
maxi = -1
for c in colors:
    p = c.buy(prev)
    maxi = max(maxi, p)
    prev = p
print(maxi)
