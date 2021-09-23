n = int(input())
a = [[int(input())-1, False] for _ in range(n)]
a[0][1] = True
now = 0
cnt = 0
while True:
    now = a[now][0]
    if a[now][1]:
        print(-1)
        break
    a[now][1] = True
    cnt += 1
    if now == 1:
        print(cnt)
        break
