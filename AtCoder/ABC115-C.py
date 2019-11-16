n, k = map(int, input().split())

lis = []

for _ in range(n):
    lis.append(int(input()))

lis.sort()

min = 10**10
for i in range(len(lis)-k+1):
    dist = lis[i+k-1] - lis[i]
    if min > dist: min = dist
print(min)
