N = int(input())
points = []
canMove = True
mods = -1
maxi = -1
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
    if i == 0:
        mods = (x + y)%2
    elif canMove:
        if (x + y) % 2 != mods: canMove = False
    maxi = max(maxi, abs(x) + abs(y))
if not canMove:
    print(-1)
else:
    print(maxi)
    op = "1"
    for i in range(1, maxi):
        op += " 1"
    print(op)
    for p in points:
        op = ""
        i = int((maxi - (abs(p[0]) + abs(p[1]))) / 2)
        for i2 in range(i):
            op += "LR"
        while p[0] != 0:
            if p[0] > 0:
                op += "R"
                p[0] -= 1
            elif p[0] < 0:
                op += "L"
                p[0] += 1
        while p[1] != 0:
            if p[1] > 0:
                op += "U"
                p[1] -= 1
            elif p[1] < 0:
                op += "D"
                p[1] +=1
        print(op)

