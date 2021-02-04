n = int(input())
path = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    path.append([a-1,b-1])
c = list(map(int, input().split()))
c.sort(reverse=True)

result = [-1 for _ in range(n)]
path.sort(key=lambda x: x[0] * 10 + x[1])
p = path.pop(0)
result[p[0]] = c[0]
result[p[1]] = c[1]
cx = 2
while cx < n:
    for p in path:
        if result[p[0]] != -1 and result[p[1]] == -1:
            result[p[1]] = c[cx]
            path.remove(p)
            break
        elif result[p[0]] == -1 and result[p[1]] != -1:
            result[p[0]] = c[cx]
            path.remove(p)
            break
    cx += 1
large = max(c)
c.remove(large)
print(sum(c))
print(' '.join([str(v) for v in result]))