n = int(input())
aoki = 0
chokulis = []
for _ in range(n):
    a, b = map(int, input().split())
    aoki += a
    chokulis.append(a*2+b)
chokulis.sort(reverse=True)

cnt = 0
for c in chokulis:
    aoki -= c
    cnt += 1
    if aoki < 0:
        print(cnt)
        break
