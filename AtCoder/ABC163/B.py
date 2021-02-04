x, _ = map(int,input().split())
a = list(map(int,input().split()))
y = x - sum(a)
if y < 0:
    print(-1)
else:
    print(y)
