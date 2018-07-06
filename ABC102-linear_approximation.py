n = int(input())
a = list(map(int, input().split()))
tmp = [a[x] - (x+1) for x in range(0,n)]
tmp.sort()
b = tmp[n // 2]
print(sum((abs(tmp[i] - b) for i in range(0,n))))
