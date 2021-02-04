n = int(input())
a = list(map(int,input().split()))
cnt = 0
while True:
    for idx in range(len(a)):
        if a[idx] % 2 == 0: a[idx] = a[idx] // 2
        else:
            print(cnt)
            exit()
    cnt += 1
