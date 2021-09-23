# TLE
n = int(input())
use = [[True] * (n-1) for _ in range(n)]
pcol = [0] * n
brcol = []
colors = -1

def decInt(v):
    return int(v) - 1

for _ in range(n-1):
    a, b = map(decInt, input().split())
    colo = pcol[a] if pcol[a] > pcol[b] else pcol[b]
    if use[a][colo] and use[b-1][colo]:
        use[a][colo] = False
        use[b][colo] = False
        brcol.append(colo+1)
        if pcol[a] == colo:
            for i in range(colo+1, n-1):
                if use[a][i]: 
                    pcol[a] = i
                    break
        if pcol[b] == colo:
            for i in range(colo+1, n-1):
                if use[b][i]: 
                    pcol[b] = i
                    break
        if colors < colo:
            colors = colo
print(colors+1)
for co in brcol:
    print(co)
