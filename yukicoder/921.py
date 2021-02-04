n = int(input())
a = list(map(int, input().split()))
lis = [False] * n

cnt = 1
lis[0] = True
for i in range(1,n):
    if not lis[i-1]:
        lis[i] = True
        cnt += 1
    elif a[i-1] == a[i]:
        lis[i] = True
        cnt += 1

print(cnt)
    
