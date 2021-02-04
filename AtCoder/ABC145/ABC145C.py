import math
n = int(input())
total = 0
towns = []
for _ in range(n):
    x, y = map(int, input().split())
    for t in towns:
        total += math.sqrt( (t[0]-x)**2 + (t[1]-y)**2 )
    towns.append([x,y])

print(total*2/n)
