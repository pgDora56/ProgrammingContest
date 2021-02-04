n = int(input())
a = list(map(int,input().split()))
a.sort()
amax = a[-1]
flags = [True] * amax

prev = -1

cnt = 0
for idx in range(n):
    i = a[idx]
    if prev == i: continue
    if flags[i-1]: 
        cnt += 1
        if idx < n-1:
            if i == a[idx+1]:
                cnt -= 1
    ax = i + i
    while ax <= amax:
        flags[ax-1] = False
        ax += i
    prev = i
print(cnt)
