n = int(input())
l = list(map(int,input().split()))
l.sort()

total = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        if l[i] == l[j]: continue
        w = l[i] + l[j]
        cnt = 0
        for k in range(j+1, n):
            if l[j] == l[k]: continue
            if l[k] >= w: break
            cnt += 1
        total += cnt

print(total)

