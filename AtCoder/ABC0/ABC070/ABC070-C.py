import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
ns = []
for _ in range(n):
    ns.append(int(input()))

print(lcm(ns))