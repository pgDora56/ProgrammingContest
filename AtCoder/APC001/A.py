x, y = map(int, input().split())
if x % y == 0:
    print(-1)
else:
    cnt = 1
    while True:
        if (x * cnt) % y != 0:
            print(x * cnt)
            exit()
        cnt += 1
