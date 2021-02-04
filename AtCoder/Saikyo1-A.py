m, d = map(int, input().split())
if d < 20:
    print(0)
    exit(0)

cnt = 0
for month in range(1, m + 1):
    for x in range(20, d+1):
        d10 = x // 10
        d1 = x % 10
        if d10 * d1 == month and d1 != 1:
            cnt += 1
print(cnt)

