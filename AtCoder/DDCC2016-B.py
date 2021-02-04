import math

def cut_len(line):
    global r, n, m
    h = r - (r*2/n)*line
    return 2*math.sqrt(r*r-h*h)

def cutting(line):
    another = line + m
    if abs(line-n/2) < abs(another-n/2):
        return cut_len(line)
    else:
        return cut_len(another)


r, n, m = map(int, input().split())

total = 0
for i in range(1-m, n):
    total += cutting(i)
print(total)

"""
0, 1
1, 2
2, 3
3, 4
4, 5

1-M ~ N-1

-2,
-1,2
0, 3
1, 4
2, 5
3, 6
"""
