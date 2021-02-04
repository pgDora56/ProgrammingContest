import copy

n, m = map(int,input().split())
grp = [i for i in range(n)]
value = list(map(int,input().split()))
least = copy.deepcopy(value)

paths = [[] for _ in range(n)]
for cnt in range(m):
    x, y = map(lambda x:int(x)-1, input().split())
    paths[x].append(y)

maxi = 0
maxi_initialize = False
for f in range(n):
    for t in paths[f]:
        profit = value[t] - least[f]
        if not maxi_initialize:
            maxi = profit
            maxi_initialize = True
        else:
            maxi = max(maxi, profit)
        least[t] = min(least[t], least[f])

print(maxi)
