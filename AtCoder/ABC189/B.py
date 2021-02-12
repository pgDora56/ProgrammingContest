n, x = map(int, input().split())
x *= 100
total = 0
for i in range(n):
    v, p = map(int, input().split())
    total += v * p
    if total > x:
        print(i+1)
        exit()
print(-1)
