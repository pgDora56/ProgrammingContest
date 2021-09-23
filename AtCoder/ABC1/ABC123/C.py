import math
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

l = min([a,b,c,d,e])
print(5 + math.ceil(n/l) - 1)
