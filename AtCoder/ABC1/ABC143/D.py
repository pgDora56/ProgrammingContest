import bisect
n = int(input())
tris = list(map(int,input().split()))
tris.sort()
cnt = 0
for i in range(n-2):
    a = tris[i]
    for j in range(i+1,n-1):
        b = tris[j]
        r = bisect.bisect_left(tris, a+b)
        cnt += r - j - 1
print(cnt)
