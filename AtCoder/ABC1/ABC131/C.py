import math
def lcm(x, y):
    return (x * y) // math.gcd(x,y)
a,b,c,d = map(int,input().split())
a -= 1
e = lcm(c,d)
print(b-a-b//c-b//d+b//e+a//c+a//d-a//e)

