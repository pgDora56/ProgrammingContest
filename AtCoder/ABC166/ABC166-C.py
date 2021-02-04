n, m = map(int,input().split())
h = list(map(int,input().split()))
good = [True] * n
for _ in range(m):
    a,b = map(lambda x:int(x)-1,input().split())
    if h[a] < h[b]:
        good[a] = False
    elif h[a] > h[b]:
        good[b] = False
    else:
        good[a] = False
        good[b] = False
print(good.count(True))
