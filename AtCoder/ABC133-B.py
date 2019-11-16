from math import sqrt
n, d = map(int, input().split())
dots = []
for i in range(n):
    dot = list(map(int, input().split()))
    dots.append(dot)
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        distance = 0
        for dm in range(d):
            distance += pow(dots[i][dm] - dots[j][dm],2)
        dis = sqrt(distance)
        if int(dis) - dis == 0:
            cnt += 1
print(cnt)