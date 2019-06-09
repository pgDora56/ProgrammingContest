n = int(input())
v = list(map(int, input().split()))
c = list(map(int,input().split()))
total = 0
for i in range(n):
    if v[i] - c[i] > 0: total += v[i] - c[i]
print(total)