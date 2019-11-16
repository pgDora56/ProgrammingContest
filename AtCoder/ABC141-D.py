n, m = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(m):
    buy = max(a)
    a.remove(buy)
    a.append(int(buy/2))
print(sum(a))
