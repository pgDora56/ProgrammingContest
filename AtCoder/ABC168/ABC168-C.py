from math import cos, sin, sqrt, radians
a, b, h, m = map(int,input().split())
hm = 60 * h + m
angled = abs(hm / 2 - 6 * m)
angle = radians(angled)
x = pow(a-b*cos(angle), 2)
y = pow(b*sin(angle),2)
print(sqrt(x+y))
