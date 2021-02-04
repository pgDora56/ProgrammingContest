n, m = map(int,input().split())
roads = [0] * n
for _ in range(m):
    i = list(map(lambda x:int(x)-1,input().split()))
    for ix in i: roads[ix] += 1
for x in roads: print(x)
