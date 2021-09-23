k, n = map(int, input().split())
a = list(map(int, input().split()))
distances = []

for i in range(len(a)):
    d = a[i] - a[i-1]
    if i == 0:
        d += k
    distances.append(d)
print(sum(distances) - max(distances))


