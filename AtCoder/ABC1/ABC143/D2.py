import bisect
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for a in range(n-2):
    for b in range(a+1, n-1):
        ab = L[a] + L[b]
        r = bisect.bisect_left(L, ab)
        l = b + 1
        ans += r - l
print(ans)
