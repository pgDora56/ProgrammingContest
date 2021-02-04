n = int(input())
limits = []
t = 0
for _ in range(5):
    limits.append(int(input()))
for i in range(5):
    last_n = n % limits[i]
    t += (n - last_n) / limits[i] + 1
    n = last_n
print(int(t))