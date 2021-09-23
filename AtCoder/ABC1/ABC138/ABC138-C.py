n = int(input())
v = list(map(int, input().split()))
v.sort()
for idx in range(1, n):
    v[idx] = (v[idx-1] + v[idx]) / 2
print(v[-1])