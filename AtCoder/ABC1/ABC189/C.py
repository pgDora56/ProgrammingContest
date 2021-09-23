n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    x = a[i]
    for r in range(i, n):
        x = min(x, a[r])
        ans = max(ans, x*(r-i+1))

print(ans)
