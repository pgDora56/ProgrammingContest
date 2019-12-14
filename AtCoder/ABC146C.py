a, b, x = map(int, input().split())

def check(n):
    global a,b
    d = len(str(n))
    return (a * n + b * d) <= x 

btm = 0
top = 10**9

while top - btm > 1:
    mid = int((btm+top)/2)
    if check(mid):
        btm = mid
    else:
        top = mid - 1
if check(top): print(top)
else: print(btm)
