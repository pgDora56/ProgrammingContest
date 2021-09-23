a, b, c = map(int, input().split())

cnt = 0
day = 0

while cnt < c:
    day += 1
    cnt += a
    if day % 7 == 0:
        cnt += b

print(day)
