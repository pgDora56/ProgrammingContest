n = int(input())
f = []
p = []
for _ in range(n):
    f.append(list(map(int, input().split())))

for _ in range(n):
    p.append(list(map(int, input().split())))

result = -float('inf')
for i in range(1,1024):
    working = [0 for _ in range(n)]
    for j in range(10):
        if i>>j&1:
            for shop in range(n):
                if f[shop][j]:
                    working[shop] += 1
    benefit = 0
    for shop in range(n):
        benefit += p[shop][working[shop]]

    result = max([result, benefit])

print(result)