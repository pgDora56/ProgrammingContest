N = int(input())
lis = []
lstipt = []
cnt = 0
h = 0
while h == 0:
    x, y, h = map(int, input().split())
    if h == 0:
        lstipt.append([x,y,h])
    cnt += 1

for Cx in range(101):
    for Cy in range(101):
        Ph = abs(x-Cx) + abs(y-Cy) + h
        lis.append([Cx,Cy,Ph])

for _ in range(N-cnt):
    x, y, h = map(int, input().split())
    newlis = []
    if h == 0: 
        for l in lis:
            if abs(x-l[0]) + abs(y-l[1]) + h >= l[2]:
                newlis.append(l)
    else:
        for l in lis:
            if abs(x-l[0]) + abs(y-l[1]) + h == l[2]:
                newlis.append(l)
    lis = newlis

for ipt in lstipt:
    x, y, h = ipt[0], ipt[1], ipt[2]
    newlis = []
    if h == 0: 
        for l in lis:
            if abs(x-l[0]) + abs(y-l[1]) + h >= l[2]:
                newlis.append(l)
    else:
        for l in lis:
            if abs(x-l[0]) + abs(y-l[1]) + h == l[2]:
                newlis.append(l)
    lis = newlis

print(" ".join(map(str,lis[0])))

