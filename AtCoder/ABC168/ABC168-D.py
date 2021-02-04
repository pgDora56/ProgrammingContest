import sys
n, m = map(int,input().split())
mark = [-2] * (n-1)
dist = [0] * (n-1)
path = [[] for _ in range(n-1)]
path0 = []

for _ in range(m):
    a, b = map(lambda x: int(x)-2, input().split())
    if a == -1:
        path0.append(b)
        dist[b] = 1
        mark[b] = -1
    elif b == -1:
        path0.append(a)
        dist[a] = 1
        mark[a] = -1
    else:
        path[a].append(b)
        path[b].append(a)

while len(path0) > 0:
    i = path0.pop(0)
    d = dist[i]
    for p in path[i]:
        if dist[p] > d + 1 or dist[p] == 0:
            dist[p] = d + 1
            mark[p] = i
            path0.append(p)

print("Yes")
for i in mark: print(i+2)
