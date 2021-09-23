import heapq

xi = 0
yi = 0
zi = 0
def next(i):
    global xi, yi, zi, p, q, r
    if i == 0:
        xi += 1
        return heapq.nlargest(xi, p)[-1]
    elif i == 1:
        yi += 1
        return heapq.nlargest(yi, q)[-1]
    else:
        zi += 1
        return heapq.nlargest(zi, r)[-1]

x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

ns = [next(0), next(1), next(2)]

val = 0

while x + y - xi - yi - zi + 3 > 0:
    if ns[0] >= ns[1] and ns[0] >= ns[2]:
        val += ns[0]
        if len(p) > 0 and x - xi > 0:
            ns[0] = next(0)
        else:
            xi += 1
            ns[0] = 0
    elif ns[0] <= ns[1] and ns[1] >= ns[2]:
        val += ns[1]
        if len(q) > 0 and y - yi > 0:
            ns[1] = next(1)
        else:
            yi += 1
            ns[1] = 0
    else:
        val += ns[2]
        if len(r) > 0:
            ns[2] = next(2)
        else:
            ns[2] = 0
    # print(f"val:{val} x:{xi} y:{yi} z:{zi}")

print(val)
