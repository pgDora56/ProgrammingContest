import fractions
from functools import reduce

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

n, x0 = map(int, input().split())
x = list(map(int,input().split()))
x.append(x0)
x.sort()
xdiff = []
tmp = x[0]
for xs in x:
    if xs - tmp == 0: continue
    xdiff.append(xs-tmp)
print(gcd_list(xdiff))