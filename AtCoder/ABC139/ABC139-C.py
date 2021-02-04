n = int(input())
h = list(map(int, input().split()))

cnt = 0
maxi = 0
for i in range(1, len(h)):
    if h[i] <= h[i-1]:
        cnt += 1
    else:
        if maxi < cnt: maxi = cnt
        cnt = 0
print(max(maxi, cnt))
