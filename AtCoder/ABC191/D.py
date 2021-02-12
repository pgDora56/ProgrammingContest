import math
x, y, r = map(float, input().split())
x1000 = int(x * 1000)
y1000 = int(y * 1000)
r1000 = int(r*1000)
double_r1000 = r1000*r1000
# double_r = r*r
total = 0
for l in range(math.ceil(y-r) * 1000, (math.floor(y+r)+1) * 1000):
    d = math.sqrt(double_r - pow(y-l, 2))
    big = math.floor(x+d)
    small = math.ceil(x-d)
    if big >= small:
        total += big - small + 1
        print(f"Line:{l}, {small}~{big}")
print("TOTAL", total)
