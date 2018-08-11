n = int(input())
for _ in range(n):
    x = list(map(int, input().split()))
    x.sort()
    if x[0] * x[0] + x[1] * x[1] == x[2] * x[2]: print("YES")
    else: print("NO")