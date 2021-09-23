from math import floor
a,b,n = map(int,input().split())
if a == 1 or b == 1:
    print(0)
    exit()

prev = 0

for x in range(min(b-1,n),n+1, b):
    val = floor(a*x/b) - a*floor(x/b)
    if val < prev:
        print(prev)
        exit()
    prev = val

val = floor(a*n/b) - a*floor(n/b)
print(max(prev,val))

