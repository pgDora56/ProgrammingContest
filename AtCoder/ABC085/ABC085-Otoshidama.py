n, yen = map(int, input().split())
a, b, c = -1, -1, -1
for i in range(n+1):
    for j in range(i+1):
        x = n-i
        y = i-j
        z = j
        if (x * 10000 + y * 5000 + z * 1000 == yen):
            a, b, c = x, y, z
            break
    if a != -1: break
print("{} {} {}".format(a,b,c))