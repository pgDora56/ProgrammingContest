n, m = map(int, input().split())
a = list(map(int, input().split()))
t = [0]
v = 0
b = {0:1}
for i in range(n):
    v = (v + a[i]) % m
    if v in b.keys():
        b[v] += 1
    else:
        b[v] = 1
ans = 0
for i in b.values():
    ans += i * (i-1) / 2
print(int(ans))
