half = int(int(input())/2)
d = list(map(int, input().split()))
d.sort()
print(d[half]-d[half-1])

