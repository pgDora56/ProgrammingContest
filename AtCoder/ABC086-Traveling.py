n = int(input())
t, x, y = 0, 0, 0
for i in range(n):
    ti, xi, yi = map(int, input().split())
    dt, dx, dy = ti - t, xi - x, yi - y
    delta = dt - (dx + dy)
    if delta < 0 or delta % 2 != 0:
        print("No")
        exit(0)
print("Yes")