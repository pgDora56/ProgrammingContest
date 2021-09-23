n = int(input())
a = list(input().split())

ball = []
for i in range(n, 0, -1):
    c = 2
    while i * c <= n:
        if a[i*c-1] == "1":
            a[i-1] = "1" if a[i-1] == "0" else "0"
        c += 1
    if a[i-1] == "1":
        ball.append(str(i))

print(len(ball))
if ball != []: print(" ".join(ball))
